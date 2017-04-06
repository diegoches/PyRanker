from loaders.load_from_file import LoadFromFile
from rank_aggregation_methods.method_comb_max import RankCombMAX
from rank_aggregation_methods.method_comb_med import RankCombMED
from rank_aggregation_methods.method_comb_min import RankCombMIN


def main():

    print 'Hello Rank Aggregation'
    datasets = ['datasets/sample_1.txt', 'datasets/sample_2.txt']
    rl = LoadFromFile.load_ranks(datasets)
    # print rl

    ra = RankCombMED()
    ra.load_rank_list(rl)
    print ra.rank()
    print '----'
    rm = RankCombMIN()
    rm.load_rank_list(rl)
    print rm.rank()
    print '----'
    rm = RankCombMAX()
    rm.load_rank_list(rl)
    print rm.rank()
    print '****'
    print rl

main()
