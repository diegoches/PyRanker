from rank_structures.rank import Rank


class AggregatedRank(object):

    def __init__(self):
        self.rank_list = []
        self.rank_quantity = 0

    def __str__(self):
        str_result = 'quantity: {quantity} \nranks: {ranks}'
        return str_result.format(quantity=self.rank_quantity,
                                 ranks=self.rank_list)

    def add_rank(self, rank):
        if isinstance(rank, Rank):
            self.rank_list.append(rank)
            self.rank_quantity += 1
        else:
            raise TypeError('rank is not of Rank class')
