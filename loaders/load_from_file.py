
class LoadFromFile(object):
    __positions = {
        'sim': 0,
        'id': 1
    }

    @classmethod
    def load_single_file(cls, file_name):
        try:
            file_iterator = (x for x in open(file_name))
        except IOError as e:
            print 'Error: can\'t find file or read data'
            print e
            exit(1)
        else:
            for line in file_iterator:
                print line
