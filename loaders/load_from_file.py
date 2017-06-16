from rank_structures.rank_list import RankList
from rank_structures.rank_element import RankElement
from rank_structures.rank import Rank


class LoadFromFile(object):

    @classmethod
    def validate_attributes_order(cls, attributes_order):

        has_correct_3 = 's' in attributes_order and 'i' in attributes_order

        has_correct_2 = 'i' in attributes_order and \
                        ('r' in attributes_order or 's' in attributes_order)

        if len(attributes_order) == 3:
            if has_correct_3:
                return True
            else:
                return False
        elif len(attributes_order) == 2:
            if has_correct_2:
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def get_rank_values(cls, split_line, attributes_order):
        current_similitude = None
        current_id = None
        current_rank = None

        for i, c in enumerate(attributes_order):
            if c == 's':
                current_similitude = float(split_line[i])
            elif c == 'i':
                current_id = split_line[i]
            elif c == 'r':
                current_rank = split_line[i]

        return current_similitude, current_id, current_rank

    @classmethod
    def load_single_file(cls, file_name, delimiter=None,
                         attributes_order='si'):
        try:
            if not cls.validate_attributes_order(attributes_order):
                raise RuntimeError('Not valid attribute order: {0}'.format(
                    attributes_order))

            file_iterator = (x for x in open(file_name))
            order = 1
            current_rank = Rank()

            for line in file_iterator:
                if delimiter:
                    split_line = line.split(delimiter)
                else:
                    split_line = line.split()

                current_similitude, current_id, current_element_rank = \
                    cls.get_rank_values(split_line, attributes_order)

                if current_element_rank:
                    current_rank_element = RankElement(current_similitude,
                                                       current_id,
                                                       current_element_rank)
                else:
                    current_rank_element = RankElement(current_similitude,
                                                       current_id, order)

                current_rank.add_element(current_rank_element)
                order += 1
            return current_rank
        except IOError as e:
            print 'Error: can\'t find file or read data'
            print e
            exit(1)
        except TypeError as e:
            print 'Error: can\'t load data correctly'
            print e
            exit(1)

    @classmethod
    def load_ranks(cls, file_list):
        try:
            rank_list = RankList()
            for current_file in file_list:
                current_rank = cls.load_single_file(current_file)
                rank_list.add_rank(current_rank)
            return rank_list
        except TypeError as e:
            print 'Error: can\'t load data correctly'
            print e
            exit(1)
