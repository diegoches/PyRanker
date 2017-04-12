# -*- coding: utf-8 -*- #

from rank_aggregation import RankAggregation
import operator


# The RA_CombSUM class handles the CombSUM algorithm for Rank Aggregation.
# This class inherits from the RankAggregation class, and implements the
# rank() function.
# The CombSUM algorithm sums for each object its currents similarities in each
# ranked list, and then it order them in descending order.
# \cite Fox:1994 .
class RankCombSUM(RankAggregation):
    # \fn rank
    # The rank function uses the CombSUM algorithm to compute a new ranked
    # list for the query object.
    # \param tp_param The CombSUM algorithm does not use any hyper-parameter.
    # \return A ranked list with the same structure as the ls_data attribute
    def rank(self, *tp_param):

        # Sums the similarities of each object in a dictionary where each key
        # is the id of each object.
        temporal_dictionary = {}
        for current_rank  in self.rank_list.ranks:
            for element in current_rank.rank:
                if element.id in temporal_dictionary:
                    temporal_dictionary[element.id] += element.similitude
                else:
                    temporal_dictionary[element.id] = element.similitude

        self.aggregated_rank.add_dictionary(temporal_dictionary)
        return self.aggregated_rank
