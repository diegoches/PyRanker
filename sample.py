from loaders.load_from_file import LoadFromFile


def main():

    print 'Hello Rank Aggregation'
    datasets = ['datasets/sample_1.txt', 'datasets/sample_2.txt']
    print LoadFromFile.load_ranks(datasets)

main()
