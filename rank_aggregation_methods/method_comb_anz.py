# -*- coding: utf-8 -*- #

from rank_aggregation import RankAggregation
import operator


# The RA_CombANZ class handles the CombANZ algorithm for Rank Aggregation.
# This class inherits from the RankAggregation class,
# and implements the rank() function.
# The CombANZ algorithm divide the sum of the objects similarities
# in each ranked list by the number of non zero similarities of each object,
# and then it order them in descending order.
# \cite Fox:1994 .
class RankCombANZ(RankAggregation):
    # \fn rank
    # The rank function uses the CombANZ algorithm to compute a new ranked
    # list for the query object.
    # \param tp_param The CombANZ algorithm does not use any hyper-parameter.
    # \return A ranked list with the same structure as the ls_data attribute
    def rank(self, *tp_param):

        # Sums the similarities of each object in a dictionary where each key
        # is the id of each object, and counts the non zero similarities.
        temporal_dictionary = {}
        count_dictionary = {}
        for current_rank in self.rank_list.ranks:
            for element in current_rank.rank:
                if element.similitude > 0:
                    if element.id not in count_dictionary:
                        count_dictionary[element.id] = 1
                    else:
                        count_dictionary[element.id] += 1
                if element.id in temporal_dictionary:
                    temporal_dictionary[element.id] += element.similitude
                else:
                    temporal_dictionary[element.id] = element.similitude

        # Divides the new similarity of each element by its quantity of
        # non zero similarities.
        for k, v in temporal_dictionary.items():
            if k in count_dictionary:
                temporal_dictionary[k] = v / count_dictionary[k]
            else:
                temporal_dictionary[k] = 0

        self.aggregated_rank.add_dictionary(temporal_dictionary)
        return self.aggregated_rank
