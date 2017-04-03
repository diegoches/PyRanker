from loaders.load_from_file import LoadFromFile
from rank_aggregation_methods.method_comb_med import RankCombMed


def main():

    print 'Hello Rank Aggregation'
    datasets = ['datasets/sample_1.txt', 'datasets/sample_2.txt']
    rl = LoadFromFile.load_ranks(datasets)
    # print rl

    ra = RankCombMed()
    ra.load_rank_list(rl)
    ra.rank()
    print ra.aggregated_rank
    print '****'
    print rl

main()
