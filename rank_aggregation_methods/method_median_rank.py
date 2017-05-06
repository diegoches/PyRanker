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
    # (a list of dictionaries, each dictionary with three keys
    # ('sim','id','rank')).
    def rank(self, *tp_param):

        dict_mapper = {}
        for e in self.rank_list.ranks[0].rank:
            dict_mapper[e.id] = [e.rank]

        for i in xrange(1, self.rank_list.ranks_quantity):
            for e in self.rank_list.ranks[i].rank:
                dict_mapper[e.id].append(e.rank)

        # for k,v in dict_mapper.items():



        # --------------------------------

        # define median type function
        if self.int_num_ranks % 2 == 0:  # even
            func_median = self.__median_even
            self.median_index1 = (self.int_num_ranks / 2) - 1
            self.median_index2 = self.median_index1 + 1
        else:  # odd
            func_median = self.__median_odd
            self.median_index = ((self.int_num_ranks + 1) / 2) - 1

        dc_map = {}

        # initialize map of ranks from first ranked list
        for dc_i in self.ls_data[0]:
            dc_map.update({dc_i.get('id'): [dc_i.get('rank')]})

        # Add positons of others ranked lists
        for i in range(1, self.int_num_ranks):
            for dc_i in self.ls_data[i]:
                dc_map[dc_i.get('id')].append(dc_i.get('rank'))

        # Computes median
        for str_id in dc_map.iterkeys():
            dc_map[str_id] = func_median(dc_map[str_id])

        max_median = max(dc_map.values())

        # Sorting objects by using the median values
        dc_map = sorted(dc_map.items(), key=lambda dc_map: dc_map[1])

        ls_final_rank = []

        # The new similarity is the normalized median.
        for i in range(len(dc_map)):
            norm_median = 1 - dc_map[i][1] / float(max_median)
            ls_final_rank.append(
                {'id': dc_map[i][0], 'rank': i + 1, 'sim': norm_median})

        return ls_final_rank

    # \fn __odd
    # Calculates the median for an odd number of values.
    # \param ls_ranks A list of numbers.
    # \return The median of ls_rank.
    def __median_odd(self, ls_ranks):
        return sorted(ls_ranks)[self.median_index]

    # \fn __even
    # Calculates the median for an even number of values.
    # \param ls_ranks A list of numbers.
    # \return The median of ls_rank
    def __median_even(self, ls_ranks):
        ls_tmp = sorted(ls_ranks)
        return (ls_tmp[self.median_index1] + ls_tmp[self.median_index2]) / 2.0

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

