# -*- coding: utf-8 -*- #

from rank_aggregation import RankAggregation
import math


# The RA_MScores class handles the Multiplication scores (MS) method for
# Rank Aggregation.
# This class inherits from the RankAggregation class, and implements the
# rank() function.
# The Multiplication Scores algorithm works by multiplying the different
# similarity scores, high scores are propagated to the others, leading to
# high aggregated values. The similarity multiplication can be seen as the
# computation of the probability of two objects be similar.
# \cite Pedronette:14 .
class RankMScores(RankAggregation):
    # \fn rank
    # The rank function uses the Multiplication Scores algorithm to compute a
    # new ranked list for the query object.
    # \param tp_param The Multiplication Scores algorithm does not use any
    # hyper-parameter.
    # \return A ranked list with the same structure as the ls_data attribute
    def rank(self, *tp_param):

        dict_mapper = {}

        # initialize map of similarities from first ranked list
        for e in self.rank_list.ranks[0].rank:
            dict_mapper[e.id] = e.similitude + 1

        # Multiplication scores
        for i in xrange(1, self.rank_list.ranks_quantity):
            for e in self.rank_list.ranks[i].rank:
                dict_mapper[e.id] *= e.similitude + 1

        # m root of scores
        for k, v in dict_mapper.items():
            dict_mapper[k] = \
                math.pow(v, 1.0/self.rank_list.ranks_quantity) / float(self.rank_list.ranks_quantity)

        # The new similarity is the normalized scores.
        max_score = max(dict_mapper.values())
        for k, v in dict_mapper.items():
            dict_mapper[k] = v / float(max_score)

        self.aggregated_rank.add_dictionary((dict_mapper))
        return self.aggregated_rank

        # ----------------

        # dc_map = {}
        #

        # for dc_i in self.ls_data[0]:
        #     dc_map.update({dc_i.get('id'): (dc_i.get('sim') + 1)})
        #
        #
        # for i in range(1, self.int_num_ranks):
        #     for dc_i in self.ls_data[i]:
        #         dc_map[dc_i.get('id')] *= dc_i.get('sim') + 1
        #
        #
        # for str_id in dc_map.iterkeys():
        #     dc_map[str_id] = math.pow(dc_map[str_id],
        #                               1.0 / self.int_num_ranks) / float(
        #         self.int_num_ranks)
        #
        # max_count = max(dc_map.values())
        #
        # # Sorting objects by using scores
        # dc_map = sorted(dc_map.items(), key=lambda dc_map: dc_map[1],
        #                 reverse=True)
        #
        # ls_final_rank = []
        #
        # # The new similarity is the normalized scores.
        # for i in range(len(dc_map)):
        #     final_count = dc_map[i][1] / float(max_count)
        #     ls_final_rank.append(
        #         {'id': dc_map[i][0], 'rank': i + 1, 'sim': final_count})
        #
        # return ls_final_rank
