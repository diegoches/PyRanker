from loaders.load_from_file import LoadFromFile
from rank_aggregation_methods.method_borda import RankBorda
from rank_aggregation_methods.method_comb_anz import RankCombANZ
from rank_aggregation_methods.method_comb_max import RankCombMAX
from rank_aggregation_methods.method_comb_med import RankCombMED
from rank_aggregation_methods.method_comb_min import RankCombMIN
from rank_aggregation_methods.method_comb_mnz import RankCombMNZ
from rank_aggregation_methods.method_comb_sum import RankCombSUM
from rank_aggregation_methods.method_copeland import RankCopeland
from rank_aggregation_methods.method_footrule import RankFootrule
from rank_aggregation_methods.method_median_rank import RankMedianRank
from rank_aggregation_methods.method_mscores import RankMScores
from rank_aggregation_methods.method_reciprocal import RankReciprocal


# ----------------------------------------------------------------------------------------------------------------- #
# This file shows a small example of how to load data using PyRanker, and applying all the Rank Aggregation Methods.
# ----------------------------------------------------------------------------------------------------------------- #

def main():

    datasets = ['datasets/sample_1.txt', 'datasets/sample_2.txt', 'datasets/sample_3.txt']
    rl = LoadFromFile.load_ranks(datasets)
    # print rl

    # ra = LoadFromFile.load_single_file('datasets/sample_4.txt')
    # print ra
    # ra.process_rank()
    # print ra

    # print '--RankCombMED--'
    # ra = RankCombMED()
    # ra.load_rank_list(rl)
    # print ra.rank()
    # print '--RankCombMIN--'
    # rm = RankCombMIN()
    # rm.load_rank_list(rl)
    # print rm.rank()
    # print '--RankCombMAX--'
    # rm = RankCombMAX()
    # rm.load_rank_list(rl)
    # print rm.rank()
    # print '--RankCombMNZ--'
    # rm = RankCombMNZ()
    # rm.load_rank_list(rl)
    # print rm.rank()
    # print '--RankCombSUM--'
    # rm = RankCombSUM()
    # rm.load_rank_list(rl)
    # print rm.rank()
    # print '--RankCombANZ--'
    # rm = RankCombANZ()
    # rm.load_rank_list(rl)
    # print rm.rank()
    # print '--RankFootrule--'
    # rm = RankFootrule()
    # rm.load_rank_list(rl)
    # print rm.rank()
    # print '--RankBorda--'
    # rm = RankBorda()
    # rm.load_rank_list(rl)
    # print rm.rank()
    # print '--RankMScores--'
    # rm = RankMScores()
    # rm.load_rank_list(rl)
    # print rm.rank()
    # print '--RankMedianRank--'
    # rm = RankMedianRank()
    # rm.load_rank_list(rl)
    # print rm.rank()
    # print '--RankReciprocal 0--'
    # rm = RankReciprocal()
    # rm.load_rank_list(rl)
    # print rm.rank(0)
    # print '--RankReciprocal 1--'
    # rm = RankReciprocal()
    # rm.load_rank_list(rl)
    # print rm.rank(1)
    # print '--RankCopeland--'
    # rm = RankCopeland()
    # rm.load_rank_list(rl)
    # print rm.rank()
    # print '****'
    # print rl

main()
