# -*- coding: utf-8 -*- #

from rank_aggregation import RankAggregation
import numpy as np


# The RA_Copeland class handles the Copeland algorithm for Rank Aggregation.
# This class inherits from the RankAggregation class, and implements the
# rank() function.
# The Copeland algorithm compare each pair of objects and determine which one
# is more preferred. The more preferred object is awarded with 1 point.
# If there is a tie, each object is awarded with 0.5 point. After all
# pairwise comparisons are made, the candidate with the most points
# (the most pairwise wins) is declared the winner.
# \cite Lippman:2012 .
class RankCopeland(RankAggregation):

    # \fn rank
    # The rank function uses the Copeland algorithm to compute a new
    # ranked list for the query object.
    # \param tp_param The CombANZ algorithm does not use any hyper-parameter.
    # \return A ranked list with the same structure as the ls_data attribute
    # (a list of dictionaries, each dictionary with three keys
    # ('sim','id','rank')).
    def rank(self, *tp_param):

        dict_mapper = {}
        ranks_size = self.get_ranks_size()

        # Create the score matrix
        score_matrix = np.zeros((ranks_size, ranks_size))

        # Initialize the score matrix (comparisons) and compute the scores
        # for the first rank aggregation
        for e in self.get_rank_by_index(0):
            dict_mapper[e.id] = e.rank
            for i in xrange(e.rank, ranks_size):
                score_matrix[e.rank-1][i] += 1

        # Compute the comparisons for the others ranked list
        for i in xrange(1, self.get_ranks_quantity()):
            winners_list = []
            for e in self.get_rank_by_index(i):
                row = dict_mapper[e.id] - 1
                for column in xrange(ranks_size):
                    if column not in winners_list and row != column:
                        score_matrix[row][column] += 1
                winners_list.append(row)

        # Compute the points for each element according to the score matrix
        points_list = [0 for a in xrange(ranks_size)]
        for i in xrange(ranks_size):
            for j in xrange(i+1, ranks_size):
                if score_matrix[i][j] > self.get_ranks_quantity()/2.0:
                    points_list[i] += 1
                else:
                    points_list[j] += 1

        # Build rank aggregated list result and compute the similarity value
        dict_result = {}
        points_max = max(points_list)
        for e, p in zip(self.get_rank_by_index(0), points_list):
            dict_result[e.id] = p/float(points_max)

        self.aggregated_rank.add_dictionary(dict_result)
        return self.aggregated_rank
