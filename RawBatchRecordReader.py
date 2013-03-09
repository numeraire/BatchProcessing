__author__ = 'blocke'


class RawBatchRecordReader(object):

    def __init__(self, file_location):
        f = open(file_location, "r")

        f.close()