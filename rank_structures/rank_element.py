class RankElement(object):

    def __init__(self, similitude, element_id, rank_order):
        self.similitude = similitude
        self.id = element_id
        self.rank = rank_order

    def __str__(self):
        str_result = '{rank}:{id}|{similitude}'
        return str_result.format(rank=self.rank, id=self.id,
                                 similitude=self.similitude)
