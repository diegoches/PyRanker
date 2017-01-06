# -*- coding: utf-8 -*- #

from RankAggregation import RankAggregation
import operator


# The RA_CombANZ class handles the CombANZ algorithm for Rank Aggregation.
# This class inherits from the RankAggregation class,
# and implements the rank() function.
# The CombANZ algorithm divide the sum of the objects similarities
# in each ranked list by the number of non zero similarities of each object,
# and then it order them in descending order.
# \cite Fox:1994 .
class RkCombANZ(RankAggregation):
    # \fn rank
    # The rank function uses the CombANZ algorithm to compute a new ranked
    # list for the query object.
    # \param tp_param The CombANZ algorithm does not use any hyper-parameter.
    # \return A ranked list with the same structure as the ls_data attribute
    # (a list of dictionaries, each dictionary with three keys
    # ('sim','id','rank')).
    def rank(self, *tp_param):

        int_tam = len(self.ls_data[0])
        int_rnk = len(self.ls_data)

        dc_tmp = {}
        dc_cont = {}

        # Sums the similarities of each object in a dictionary where each key
        # is the id of each object, and counts the non zero similarities..
        for i in range(0, int_rnk):
            for j in range(0, int_tam):
                str_name = self.ls_data[i][j].get('id')
                flo_sim = self.ls_data[i][j].get('sim')
                if flo_sim > 0:
                    if str_name not in dc_cont:
                        dc_cont[str_name] = 1
                    else:
                        dc_cont[str_name] += 1
                if str_name not in dc_tmp:
                    dc_tmp[str_name] = flo_sim
                else:
                    dc_tmp[str_name] = dc_tmp[str_name] + flo_sim

        # Divides the new similarity of each element by its quantity of
        # non zero similarities.
        for tp_param in dc_tmp.keys():
            if tp_param in dc_cont:
                dc_tmp[tp_param] = dc_tmp[tp_param] / dc_cont[tp_param]
            else:
                dc_tmp[tp_param] = 0

        # Orders a list of the objects by its new similarity.
        ls_sor = sorted(dc_tmp.iteritems(),
                        key=operator.itemgetter(1), reverse=True)

        ls_ra = []

        # Maps the new rank in the output format.                        
        for i in range(0, int_tam):
            dc_tp = {'sim': ls_sor[i][1], 'id': ls_sor[i][0], 'rank': i + 1}
            ls_ra.append(dc_tp)

        return ls_ra
