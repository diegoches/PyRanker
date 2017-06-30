class RankElement(object):

    def __init__(self, similitude, element_id, rank_order):
        # Float between 0 and 1.
        self.similitude = similitude
        # String, number that identifies the RankElement() object.
        self.id = element_id
        # Integer that denotes the order of the element in the rank that it
        # belongs to.
        self.rank = rank_order

    def __str__(self):
        str_result = '{rank}:{id}|{similitude}'
        return str_result.format(rank=self.rank, id=self.id,
                                 similitude=self.similitude)
