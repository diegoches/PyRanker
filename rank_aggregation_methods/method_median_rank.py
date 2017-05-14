# -*- coding: utf-8 -*- #

from rank_aggregation import RankAggregation


# The RA_MedianRank class handles a Median algorithm for Rank Aggregation.
# This class inherits from the RankAggregation class, and implements the
# rank() function.
# The Median algorithm finds the median of the positions from each object in
# each ranked list, and then it order them in ascending order.
# \cite Fagin:2003 .
class RankMedianRank(RankAggregation):
    # \fn rank
    # The rank function uses a Median algorithm to compute a new ranked list
    # for the query object.
    # \param tp_param The Median algorithm does not use any hyper-parameter.
    # \return A ranked list with the same structure as the ls_data attribute
    def rank(self, *tp_param):

        # initialize map of ranks from first ranked list
        dict_mapper = {}
        for e in self.rank_list.ranks[0].rank:
            dict_mapper[e.id] = [e.rank]

        # Add positons of others ranked lists
        for i in xrange(1, self.rank_list.ranks_quantity):
            for e in self.rank_list.ranks[i].rank:
                dict_mapper[e.id].append(e.rank)

        # Computes median
        for k, v in dict_mapper.items():
            dict_mapper[k] = self.get_median(v)

        # The new similarity is the normalized median.
        max_median = max(dict_mapper.values())
        for k, v in dict_mapper.items():
            dict_mapper[k] = 1 - v/float(max_median)

        self.aggregated_rank.add_dictionary(dict_mapper)
        return self.aggregated_rank

    def get_median(self, list_of_ranks):
        list_of_ranks.sort()
        size = len(list_of_ranks)
        if size % 2 == 0:
            index_1 = (size/2) - 1
            index_2 = index_1 +1
            median_1 = list_of_ranks[index_1]
            median_2 = list_of_ranks[index_2]
            median = (median_1 + median_2) / 2.0
        else:
            index = int(size/2)
            median = list_of_ranks[index]
        return median
