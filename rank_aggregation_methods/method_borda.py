# -*- coding: utf-8 -*- #

from rank_aggregation import RankAggregation


# The RA_Borda class handles the Borda algorithm for Rank Aggregation.
# This class inherits from the RankAggregation class, and implements 
# the rank() function. 
# The Borda algorithm sums for each object its currents positions in each 
# ranked list, and then it order them in ascending order.
# \cite Young:74 .
class RankBorda(RankAggregation):

    def rank(self, *tp_param):
        """
        The rank function uses the Borda algorithm to compute a new ranked
        list for the query object.
        :param tp_param: The Borda algorithm does not use any hyper-parameter.
        :return: A Rank() object that represents the ranked list result.
        """

        dict_mapper = {}

        # initialize dictionary of ranks from first ranked list.
        for e in self.rank_list.ranks[0].rank:
            dict_mapper[e.id] = e.rank

        # Computes Borda count.
        for i in xrange(1, self.rank_list.ranks_quantity):
            for re in self.rank_list.ranks[i].rank:
                dict_mapper[re.id] += re.rank

        max_count = max(dict_mapper.values())

        # The new similarity is the normalized Borda count.
        for k, v in dict_mapper.items():
            final_count = 1 - (v/float(max_count))
            dict_mapper[k] = final_count

        self.aggregated_rank.add_dictionary(dict_mapper)
        return self.aggregated_rank
