# -*- coding: utf-8 -*- #

from rank_aggregation import RankAggregation


# The RA_CombMED class handles the CombMED algorithm for Rank Aggregation.
# This class inherits from the RankAggregation class,
# and implements the rank() function.
# The CombMED algorithm compute the mean of the similarities of each object
# in each ranked list, and then it order them in descending order.
# \cite Fox:1994 .
class RankCombMED(RankAggregation):
    # \fn rank
    # The rank function uses the CombMED algorithm to compute a new ranked
    # list for the query object.
    # \param tp_param The CombMED algorithm does not use any hyper-parameter.
    # \return A rank
    def rank(self, *tp_param):

        # Sums the similarities of each object in a dictionary where each
        # key is the id of each object.
        temporal_dictionary = {}
        for current_rank in self.rank_list.ranks:
            for element in current_rank.rank:
                if element.id in temporal_dictionary:
                    temporal_dictionary[element.id] += element.similitude
                else:
                    temporal_dictionary[element.id] = element.similitude

        # Get the mean similarity of each object
        ranks_quantity = self.rank_list.ranks_quantity
        for k, v in temporal_dictionary.items():
            temporal_dictionary[k] = v/ranks_quantity

        self.aggregated_rank.add_dictionary(temporal_dictionary)
        return self.aggregated_rank
