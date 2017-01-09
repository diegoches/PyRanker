# -*- coding: utf-8 -*- #

from RankAggregation import RankAggregation
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
class RkCopeland(RankAggregation):

    # \fn rank
    # The rank function uses the Copeland algorithm to compute a new
    # ranked list for the query object.
    # \param tp_param The CombANZ algorithm does not use any hyper-parameter.
    # \return A ranked list with the same structure as the ls_data attribute
    # (a list of dictionaries, each dictionary with three keys
    # ('sim','id','rank')).
    def rank(self, *tp_param):

        dc_data = {}
        int_size = len(self.ls_data[0])
        
        # Create the score matrix
        matrix = np.zeros((int_size, int_size))

        # Initialize the score matrix (comparisons) and compute the scores
        # for the first rank aggregation
        for dc_i in self.ls_data[0]:
            dc_data.update({dc_i.get("id"): dc_i.get("rank")})
            for int_column in range(dc_i.get("rank"), int_size):
                matrix[dc_i.get("rank")-1][int_column] += 1

        # Compute the comparisons for the others ranked list
        for int_i in range(1, self.int_numRanks):
            ls_winners = []
            for dc_i in self.ls_data[int_i]:
                int_row = dc_data.get(dc_i.get("id")) - 1
                for int_column in range(int_size):
                    if int_column not in ls_winners and int_row != int_column:
                        matrix[int_row][int_column] += 1
                ls_winners.append(int_row)
        
        # Compute the points for each element de according to the score matrix
        ls_pontos = [0] * int_size
        for int_row in range(int_size):
            for int_column in range(int_row+1, int_size):
                if matrix[int_row][int_column] > self.int_numRanks/2.0:
                    ls_pontos[int_row] += 1
                else:
                    ls_pontos[int_column] += 1
        
        # Build rank aggregated list result and compute the similarity value
        ls_result = []
        int_max = max(ls_pontos)
        for int_i in range(int_size):
            ls_result.append(self.ls_data[0][int_i].copy())
            ls_result[int_i]["sim"] = ls_pontos[int_i] / float(int_max)
        
        # Sort the result list according to similarity
        ls_result = sorted(ls_result, key=lambda ls_result: ls_result['sim'],
                           reverse=True)

        # Update the rank values
        for int_idx in range(len(ls_result)):
            ls_result[int_idx]["rank"] = int_idx + 1

        return ls_result

    # \fn __win
    # The win function returns which object is more similar (better position)
    # in the ranked list.
    # \param obj_1 First object to compare.
    # \param obj_2 Second object to compare.
    # \param ls_rank Ranked list used to compare the items.
    # \return A floating point number bigger than 0 if the first item is
    # more similar; smaller than 0 if the second is more similar; 0 if both
    # have the same similarity.
    def __win(self, obj_1, obj_2, ls_rank):
        int_rank_1 = int_rank_2 = 0
        for item in ls_rank:
            if item.get("id") == obj_1.get("id"):
                int_rank_1 = item.get("rank")
            elif item.get("id") == obj_2.get("id"):
                int_rank_2 = item.get("rank")
        return int_rank_2 - int_rank_1
