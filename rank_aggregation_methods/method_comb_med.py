# -*- coding: utf-8 -*- #

from rank_aggregation import RankAggregation
import operator


# The RA_CombMED class handles the CombMED algorithm for Rank Aggregation.
# This class inherits from the RankAggregation class,
# and implements the rank() function.
# The CombMED algorithm compute the mean of the similarities of each object
# in each ranked list, and then it order them in descending order.
# \cite Fox:1994 .
class RankCombMed(RankAggregation):
    # \fn rank
    # The rank function uses the CombMED algorithm to compute a new ranked
    # list for the query object.
    # \param tp_param The CombMED algorithm does not use any hyper-parameter.
    # \return A ranked list with the same structure as the ls_data attribute
    # (a list of dictionaries, each dictionary with three keys
    # ('sim','id','rank')).
    def rank(self, *tp_param):

        temporal_dictionary = {}
        for current_rank in self.rank_list.ranks:
            for element in current_rank.rank:
                if element.id in temporal_dictionary:
                    temporal_dictionary[element.id] += element.similitude
                else:
                    temporal_dictionary[element.id] = element.similitude

        ranks_quantity = self.rank_list.ranks_quantity
        for k, v in temporal_dictionary.items():
            temporal_dictionary[k] = v/ranks_quantity

        list_of_aggregated_rank = \
            sorted(temporal_dictionary.iteritems(),
                   key=operator.itemgetter(1), reverse=True)

        # --------------------------------------------------------------------

        # int_tam = len(self.ls_data[0])
        # int_rnk = len(self.ls_data)
        #
        # dc_tmp = {}
        #
        # # Sums the similarities of each object in a dictionary where each
        # # key is the id of each object.
        # for i in xrange(0, int_rnk):
        #     for j in xrange(0, int_tam):
        #         str_name = self.ls_data[i][j].get('id')
        #         flo_sim = self.ls_data[i][j].get('sim')
        #         if str_name not in dc_tmp:
        #             dc_tmp[str_name] = flo_sim
        #         else:
        #             dc_tmp[str_name] = dc_tmp[str_name] + flo_sim
        #
        # # Get the mean similarity of each object
        # for v in dc_tmp:
        #     dc_tmp[v] /= int_rnk
        #
        # # Orders a list of the objects by its new similarity.
        # ls_sor = sorted(dc_tmp.iteritems(), key=operator.itemgetter(1),
        #                 reverse=True)
        #
        # ls_ra = []
        #
        # # Maps the new rank in the output format.
        # for i in xrange(0, int_tam):
        #     dc_tp = {'sim': ls_sor[i][1], 'id': ls_sor[i][0], 'rank': i + 1}
        #     ls_ra.append(dc_tp)

        # return ls_ra
