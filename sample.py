from loaders.load_from_file import LoadFromFile
from rank_aggregation_methods.method_comb_anz import RankCombANZ
from rank_aggregation_methods.method_comb_max import RankCombMAX
from rank_aggregation_methods.method_comb_med import RankCombMED
from rank_aggregation_methods.method_comb_min import RankCombMIN
from rank_aggregation_methods.method_comb_mnz import RankCombMNZ
from rank_aggregation_methods.method_comb_sum import RankCombSUM


def main():

    print 'Hello Rank Aggregation'
    datasets = ['datasets/sample_1.txt', 'datasets/sample_2.txt']
    rl = LoadFromFile.load_ranks(datasets)
    # print rl

    print '--RankCombMED--'
    ra = RankCombMED()
    ra.load_rank_list(rl)
    print ra.rank()
    print '--RankCombMIN--'
    rm = RankCombMIN()
    rm.load_rank_list(rl)
    print rm.rank()
    print '--RankCombMAX--'
    rm = RankCombMAX()
    rm.load_rank_list(rl)
    print rm.rank()
    print '--RankCombMNZ--'
    rm = RankCombMNZ()
    rm.load_rank_list(rl)
    print rm.rank()
    print '--RankCombSUM--'
    rm = RankCombSUM()
    rm.load_rank_list(rl)
    print rm.rank()
    print '--RankCombANZ--'
    rm = RankCombANZ()
    rm.load_rank_list(rl)
    print rm.rank()
    print '****'
    print rl

main()
