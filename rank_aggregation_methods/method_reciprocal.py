# -*- coding: utf-8 -*- #

from rank_aggregation import RankAggregation


# The RA_Reciprocal class handles the Reciprocal Rank Fusion algorithm for 
# Rank Aggregation. 
# This class inherits from the RankAggregation class, and implements the 
# rank() function. 
# The Reciprocal Rank Fusion (RRF) algorithm is a simple method for 
# combining the document rankings from multiple IR systems. 
# It uses the rank information for computing a similarity score between 
# the query object and another one.
# \cite Cormack:2009 . 
class RankReciprocal(RankAggregation):

    def rank(self, mitigation=60):
        """
        The rank function uses the RRF algorithm to compute a new ranked list
        for the query object.
        :param mitigation: Integer constant that mitigates the impact of high
        rankings by outlier systems.
        :return: Rank() object that represents the ranked list result.
        """
        if mitigation < 0:
            raise ValueError(
                'Error: Mitigation parameter must be greater than or equal '
                'to zero.')

        # Initialize map of ranks from first ranked list
        dict_mapper = {}
        for e in self.get_rank_by_index(0):
            dict_mapper[e.id] = 1.0/(mitigation + e.rank)

        # Computes RRF count
        for i in xrange(1, self.get_ranks_quantity()):
            for e in self.get_rank_by_index(i):
                dict_mapper[e.id] += 1.0/(mitigation + e.rank)

        # The new similarity is the normalized RRF count.
        max_count = max(dict_mapper.values())
        for k, v in dict_mapper.items():
            dict_mapper[k] = v/float(max_count)

        self.aggregated_rank.add_dictionary(dict_mapper)
        return self.aggregated_rank
