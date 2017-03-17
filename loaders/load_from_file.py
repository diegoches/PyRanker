
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
            order = 1
            for line in file_iterator:
                splitted_line = line.split()
                current_similitude = float(splitted_line[0])
                current_id = splitted_line[1]
                print current_similitude
                print current_id
                print order
                order += 1
