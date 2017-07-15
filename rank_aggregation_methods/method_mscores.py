# -*- coding: utf-8 -*- #

from rank_aggregation import RankAggregation
import math


# The RA_MScores class handles the Multiplication scores (MS) method for
# Rank Aggregation.
# This class inherits from the RankAggregation class, and implements the
# rank() function.
# The Multiplication Scores algorithm works by multiplying the different
# similarity scores, high scores are propagated to the others, leading to
# high aggregated values. The similarity multiplication can be seen as the
# computation of the probability of two objects be similar.
# \cite Pedronette:14 .
class RankMScores(RankAggregation):
    # \fn rank
    # The rank function uses the Multiplication Scores algorithm to compute a
    # new ranked list for the query object.
    # \param tp_param The Multiplication Scores algorithm does not use any
    # hyper-parameter.
    # \return A ranked list with the same structure as the ls_data attribute
    def rank(self, *tp_param):

        dict_mapper = {}

        # initialize map of similarities from first ranked list
        for e in self.rank_list.ranks[0].rank:
            dict_mapper[e.id] = e.similitude + 1

        # Multiplication scores
        for i in xrange(1, self.rank_list.ranks_quantity):
            for e in self.rank_list.ranks[i].rank:
                dict_mapper[e.id] *= e.similitude + 1

        # m root of scores
        for k, v in dict_mapper.items():
            dict_mapper[k] = \
                math.pow(v, 1.0/self.rank_list.ranks_quantity) / \
                float(self.rank_list.ranks_quantity)

        # The new similarity is the normalized scores.
        max_score = max(dict_mapper.values())
        for k, v in dict_mapper.items():
            dict_mapper[k] = v / float(max_score)

        self.aggregated_rank.add_dictionary((dict_mapper))
        return self.aggregated_rank
