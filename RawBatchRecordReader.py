__author__ = 'blocke'


class RawBatchRecordReader(object):

    def __init__(self, file_location):

        with open(file_location, 'r') as f:
            for line in f:
                self.trim_time_stamp_and_end(line)
            f.close()

    def trim_time_stamp_and_end(self, line):
        print line[16: -1]
