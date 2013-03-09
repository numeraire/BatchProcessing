__author__ = 'blocke'
from unittest import TestCase
from RawBatchRecordReader import RawBatchRecordReader



class TestRawBatchRecordReader(TestCase):

    def __init__(self, test_name):
        TestCase.__init__(test_name)
        self.raw = RawBatchRecordReader()



if __name__ == '__main__':
    unittest.main()