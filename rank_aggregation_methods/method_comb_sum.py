# -*- coding: utf-8 -*- #

from rank_aggregation import RankAggregation
import operator


# The RA_CombSUM class handles the CombSUM algorithm for Rank Aggregation.
# This class inherits from the RankAggregation class, and implements the
# rank() function.
# The CombSUM algorithm sums for each object its currents similarities in each
# ranked list, and then it order them in descending order.
# \cite Fox:1994 .
class RkCombSUM(RankAggregation):
    # \fn rank
    # The rank function uses the CombSUM algorithm to compute a new ranked
    # list for the query object.
    # \param tp_param The CombSUM algorithm does not use any hyper-parameter.
    # \return A ranked list with the same structure as the ls_data attribute
    # (a list of dictionaries, each dictionary with three keys
    # ('sim','id','rank')).
    def rank(self, *tp_param):

        int_tam = len(self.ls_data[0])
        int_rnk = len(self.ls_data)

        dc_tmp = {}

        # Sums the similarities of each object in a dictionary where each key
        # is the id of each object.
        for i in range(0, int_rnk):
            for j in range(0, int_tam):
                str_name = self.ls_data[i][j].get('id')
                flo_sim = self.ls_data[i][j].get('sim')
                if str_name not in dc_tmp:
                    dc_tmp[str_name] = flo_sim
                else:
                    dc_tmp[str_name] = dc_tmp[str_name] + flo_sim

        # Orders a list of the objects by its new similarity.
        ls_sor = sorted(dc_tmp.iteritems(), key=operator.itemgetter(1),
                        reverse=True)

        ls_ra = []

        # Maps the new rank in the output format.
        for i in range(0, int_tam):
            dc_tp = {'sim': ls_sor[i][1], 'id': ls_sor[i][0], 'rank': i + 1}
            ls_ra.append(dc_tp)

        return ls_ra
