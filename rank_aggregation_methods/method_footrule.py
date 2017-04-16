# -*- coding: utf-8 -*- #

import math
from rank_aggregation import RankAggregation
from rank_structures.rank_element import RankElement


# The RA_Footrule class handles the Footrule method for Rank Aggregation.
# This class inherits from the RankAggregation class, and implements the
# rank() function.
# The Footrule Optimal Aggregation algorithm is a good approximation of the
# Kemeny optimal aggregation, that can be computed in polynomial time.
# \cite Dwork:2001 .
class RankFootrule(RankAggregation):
    # \fn rank
    # The rank function uses the Footrule Optimal Aggregation algorithm to
    # compute a new ranked list for the query object.
    # \param tp_param Represent a value N, where N indicates that we are
    # interested in the first N elements in the final rank (top-N).
    # \return A ranked list with the same structure as the ls_data attribute
    def rank(self, *tp_param):

        auxiliary_dict = {}
        aggregated_dict = {}

        if self.rank_list.ranks_quantity == 2:
            half_limit = 2
        else:
            half_limit = int(math.ceil(float(self.rank_list.ranks_quantity) / 2))

        rank_size = len(self.rank_list.ranks[0])
        if len(tp_param) >= 1:
            n = tp_param[0]
        else:
            n = rank_size

        current_position = 1

        for i in xrange(rank_size):
            for current_rank in self.rank_list.ranks:
                current_rank_element = current_rank.rank[i]

                if current_rank_element.id not in auxiliary_dict and current_rank_element.id not in aggregated_dict:
                    auxiliary_dict[current_rank_element.id] = 1

                elif current_rank_element.id in auxiliary_dict:
                    auxiliary_dict[current_rank_element.id] += 1

                    if auxiliary_dict[current_rank_element.id] == half_limit:
                        aggregated_dict[current_rank_element.id] = current_position
                        new_rank_element = RankElement(None, current_rank_element.id, current_position)
                        self.aggregated_rank.add_element(new_rank_element)

                        if len(self.aggregated_rank.rank) == n:
                            return self.aggregated_rank

                        current_position += 1
                        del auxiliary_dict[current_rank_element.id]
        return self.aggregated_rank

        # -------------------------------------------------------
        # ls_final_rank = []
        # aux_dict = dict()
        # j = math.ceil(len(self.ls_data) / 2.0)
        # n = tp_param[0]
        # int_pos = 1
        #
        # for i in range(len(self.ls_data[0])):
        #     # This loop runs for each element in the rank
        #
        #     for ranked_list in self.ls_data:
        #         # This loop runs for each ranked list
        #
        #         if not ranked_list[i].get('id') in aux_dict.keys() and not \
        #                         ranked_list[i].get('id') in ls_final_rank:
        #             # The element is neither in the subset of known elements
        #             # nor in the final rank. It consists of an element not
        #             # considered yet.
        #             # The element starts with a vote.
        #             aux_dict[ranked_list[i].get('id')] = 1
        #
        #         elif ranked_list[i].get('id') in aux_dict.keys():
        #             # The element receives one more vote.
        #             aux_dict[ranked_list[i].get('id')] += 1
        #
        #             # Check if the element has the necessary number of votes.
        #             if aux_dict[ranked_list[i].get('id')] == j:
        #                 # The element is inserted in the next position
        #                 # available in the final rank
        #                 ls_final_rank.append(
        #                     {'rank': int_pos, 'id': ranked_list[i].get('id'),
        #                      'sim': None})
        #
        #                 # For the context of geocodind, in wich we are
        #                 # interested only on the first element of the rank,
        #                 # we interrupt the run when achieve the second element.
        #                 # The code allows to break the execution when
        #                 # reaches the top-n elements
        #                 # In this case, the first element is the query,
        #                 # because we are using the development set.
        #                 if len(ls_final_rank) == n:
        #                     return ls_final_rank
        #
        #                 int_pos += 1
        #                 del aux_dict[ranked_list[i].get('id')]
        #
        # return ls_final_rank
