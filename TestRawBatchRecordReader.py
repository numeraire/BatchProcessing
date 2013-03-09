from BatchProcessingExceptions import BatchRecordInvalidDataTypeException

__author__ = 'blocke'
from unittest import TestCase
from RawBatchRecordReader import RawBatchRecordReader


class TestRawBatchRecordReader(TestCase):

#    def __init__(self, test_name):
 #       TestCase.__init__(test_name)
  #      self.raw = RawBatchRecordReader("C:\\Data\\BatchData\\smd_batch_MDDS_fut_4.out")

    def test_file_does_not_exist(self):
        loc = "C:\\Data\\BatchData\\smd_batch_MDDS_fut_4.out"
        self.assertRaises(IOError, RawBatchRecordReader, loc)

    def test_file_does_not_exist(self):
        loc = "C:\\Data\\BatchData\\smd_batch_MDDS_fut.out"
        self.assertRaises(BatchRecordInvalidDataTypeException, RawBatchRecordReader, loc)

if __name__ == '__main__':
    unittest.main()