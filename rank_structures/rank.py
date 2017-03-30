from rank_structures.rank_element import RankElement


class Rank(object):

    def __init__(self):
        self.rank = []

    def __str__(self):
        rank_as_string = ''
        for e in self.rank:
            rank_as_string += str(e) + '\n'

        return rank_as_string

    def add_element(self, rank_element):
        if isinstance(rank_element, RankElement):
            self.rank.append(rank_element)
        else:
            raise TypeError('rank_element is not of RankElement class')
