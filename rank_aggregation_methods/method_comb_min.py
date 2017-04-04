# -*- coding: utf-8 -*- #

from rank_aggregation import RankAggregation


# The RA_CombMIN class handles the CombMIN algorithm for Rank Aggregation.
# This class inherits from the RankAggregation class, and implements the
# rank() function.
# The CombMIN algorithm get the minimum similarity of each object in the
# ranked lists, and then it order them in descending order.
# \cite Fox:1994 .
class RankCombMIN(RankAggregation):
    # \fn rank
    # The rank function uses the CombMIN algorithm to compute a new ranked
    # list for the query object.
    # \param tp_param The CombMIN algorithm does not use any hyper-parameter.
    # \return A ranked list with the same structure as the ls_data attribute
    def rank(self, *tp_param):

        # Get the minimum similarity for each object.
        temporal_dictionary = {}
        for current_rank in self.rank_list.ranks:
            for element in current_rank.rank:
                if element.id in temporal_dictionary:
                    if element.similitude < temporal_dictionary[element.id]:
                        temporal_dictionary[element.id] = element.similitude
                else:
                    temporal_dictionary[element.id] = element.similitude

        self.aggregated_rank.add_dictionary(temporal_dictionary)
        return self.aggregated_rank
