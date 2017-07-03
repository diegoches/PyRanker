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
        """
        :param rank_index: Integer indicating the rank to which you want to
        have access.
        :return: List of rank elements representing the rank of the Rank()
        object.
        """
        return self.rank_list.ranks[rank_index].rank

    def get_ranks_quantity(self):
        """
        :return: Integer indicating the ranks quantity in the ranks list.
        """
        return self.rank_list.ranks_quantity

    def get_ranks_size(self):
        """
        :return: Integer indicating the size of each rank in the ranks list;
        in other words, the number of rank elements in each rank.
        """
        return len(self.rank_list.ranks[0])

    # \fn rank
    # This function is the one that accomplish the Rank Aggregation algorithm.
    # It has to be implemented by all the classes that inherit from this class.
    # \param tp_param is a tuple of hyper-parameters for the
    # specific algorithm. In the case that the algorithm does not have
    # hyper-parameters, tp_param would be empty.
    def rank(self, *tp_param):
        raise NotImplementedError("Please Implement this method")
