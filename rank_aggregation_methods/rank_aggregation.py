# -*- coding: utf-8 -*- #

from rank_structures.rank_list import RankList
from rank_structures.rank import Rank


class RankAggregation(object):

    def __init__(self):
        self.rank_list = RankList()
        self.aggregated_rank = Rank()

    def load_rank_list(self, rank_list):
        self.rank_list = rank_list

    def get_rank_by_index(self, rank_index):
        return self.rank_list.ranks[rank_index].rank

    def get_ranks_quantity(self):
        return self.rank_list.ranks_quantity

    # \fn rank
    # This function is the one that accomplish the Rank Aggregation algorithm.
    # It has to be implemented by all the classes that inherit from this class.
    # \param tp_param is a tuple of hyper-parameters for the
    # specific algorithm. In the case that the algorithm does not have
    # hyper-parameters, tp_param would be empty.
    def rank(self, *tp_param):
        raise NotImplementedError("Please Implement this method")
