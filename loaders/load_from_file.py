from rank_structures.rank_list import RankList
from rank_structures.rank_element import RankElement
from rank_structures.rank import Rank


class LoadFromFile(object):

    @classmethod
    def validate_attributes_order(cls, attributes_order):

        has_correct_3 = 'r' in attributes_order and 's' in attributes_order \
                        and 'i' in attributes_order

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
    def load_single_file(cls, file_name, delimiter=None,
                         attributes_order='sir'):
        try:
            file_iterator = (x for x in open(file_name))
            order = 1
            current_rank = Rank()
            for line in file_iterator:
                if delimiter:
                    split_line = line.split(delimiter)
                else:
                    split_line = line.split()
                current_similitude = float(split_line[0])
                current_id = split_line[1]
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
