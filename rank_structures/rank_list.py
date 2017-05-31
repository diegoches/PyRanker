from rank_structures.rank import Rank


class RankList(object):

    def __init__(self):
        # list of Rank() objects.
        self.ranks = []
        self.ranks_quantity = 0

    def __str__(self):
        str_result = 'Quantity: {quantity} \n\nRanks:\n\n{ranks}'
        rank_list_as_string = ''
        i = 1
        for l in self.ranks:
            rank_list_as_string += '- Rank ' + str(i) + ':\n' + str(l) + '\n'
            i += 1
        return str_result.format(quantity=self.ranks_quantity,
                                 ranks=rank_list_as_string)

    def add_rank(self, rank):
        if isinstance(rank, Rank):
            self.ranks.append(rank)
            self.ranks_quantity += 1
        else:
            raise TypeError('rank is not of Rank class')

    def get_rank(self, rank_index):
        return self.ranks[rank_index]
