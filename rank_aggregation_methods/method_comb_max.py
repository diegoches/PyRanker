# -*- coding: utf-8 -*- #

from rank_aggregation import RankAggregation
import operator


# The RA_CombMAX class handles the CombMAX algorithm for Rank Aggregation.
# This class inherits from the RankAggregation class, and implements the rank() function. 
# The CombMAX algorithm get the maximum similarity of each object in the ranked lists, and then it order them in descending order.
# \cite Fox:1994 .
class RankCombMAX(RankAggregation):

    def rank(self, *tp_param):
        """
        The rank function uses the CombMAX algorithm to compute a new ranked
        list for the query object.
        :param tp_param: The CombMAX algorithm does not use any
        hyper-parameter.
        :return: A Rank() object that represents the ranked list result.
        """
        
        # Get the maximum similarity for each object.
        temporal_dictionary = {}
        for current_rank in self.rank_list.ranks:
            for element in current_rank.rank:
                if element.id in temporal_dictionary:
                    if element.similitude > temporal_dictionary[element.id]:
                        temporal_dictionary[element.id] = element.similitude
                else:
                    temporal_dictionary[element.id] = element.similitude

        self.aggregated_rank.add_dictionary(temporal_dictionary)
        return self.aggregated_rank
