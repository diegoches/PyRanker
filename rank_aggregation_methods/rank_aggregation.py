# -*- coding: utf-8 -*- #

from rank_structures.rank_list import RankList
from rank_structures.rank import Rank


class RankAggregation(object):

    def __init__(self):
        self.rank_list = RankList()
        self.aggregated_rank = Rank()

    # \fn rank
    # This function is the one that accomplish the Rank Aggregation algorithm.
    # It has to be implemented by all the classes that inherit from this class.
    # \param tp_param is a tuple of hyper-parameters from the
    # specific algorithm. In the case that the algorithm does not have
    # hyper-parameters, tp_param would be empty.
    def rank(self, *tp_param):
        raise NotImplementedError("Please Implement this method")
