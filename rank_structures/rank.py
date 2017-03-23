from rank_structures.rank_element import RankElement


class Rank(object):

    def __init__(self):
        self.rank = []

    def __str__(self):
        return self.rank.__str__()

    def add_element(self, rank_element):
        if isinstance(rank_element, RankElement):
            self.rank.append(rank_element)
        else:
            raise TypeError('rank_element is not of RankElement class')
