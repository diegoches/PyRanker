from rank_structures.rank_element import RankElement
import operator


class Rank(object):

    def __init__(self):
        self.rank = []

    def __str__(self):
        rank_as_string = ''
        for e in self.rank:
            rank_as_string += str(e) + '\n'

        return rank_as_string

    def __len__(self):
        return len(self.rank)

    def add_element(self, rank_element):
        if isinstance(rank_element, RankElement):
            self.rank.append(rank_element)
        else:
            raise TypeError('rank_element is not of RankElement class')

    def add_dictionary(self, dictionary):
        self.rank = []
        list_of_tuples = sorted(dictionary.items(), key=operator.itemgetter(1),
                                reverse=True)
        for i, (k, v) in enumerate(list_of_tuples):
            current_rank_element = RankElement(v, k, i+1)
            self.add_element(current_rank_element)

