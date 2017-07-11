from rank_structures.rank_element import RankElement
import operator


class Rank(object):

    def __init__(self):
        # list of RankElement() objects.
        self.rank = []

    def __str__(self):
        rank_as_string = ''
        for e in self.rank:
            rank_as_string += str(e) + '\n'

        return rank_as_string

    def __len__(self):
        return len(self.rank)

    def get_element(self, element_index):
        """
        :param element_index: Integer that represents the index of a
        RankElement() object in the rank list.
        :return: A RankElement() object.
        """
        return self.rank[element_index]

    def add_element(self, rank_element):
        """
        :param rank_element: RankElement() object to be inserted in the
        current rank.
        :return: Nothing.
        """
        if isinstance(rank_element, RankElement):
            self.rank.append(rank_element)
        else:
            raise TypeError('rank_element is not of RankElement class')

    def add_dictionary(self, dictionary):
        """
        :param dictionary: Dictionary with rank element ids as keys, and its
        similarity as values.
        :return: Nothing, it fulfill the rank attribute from this Rank()
        object.
        """
        self.rank = []
        list_of_tuples = sorted(dictionary.items(), key=operator.itemgetter(1),
                                reverse=True)
        for i, (k, v) in enumerate(list_of_tuples):
            current_rank_element = RankElement(v, k, i+1)
            self.add_element(current_rank_element)

    def process_rank(self):
        """
        :return: Nothing, it sort the rank by the similitude of the
        RankElement() objects and re-assign the rank value of the
        RankElement() objects.
        """
        def helper_sort(x):
            return x.similitude
        self.rank.sort(key=helper_sort, reverse=True)
        for i, e in enumerate(self.rank):
            e.rank = i+1

