__author__ = 'blocke'
from unittest import TestCase
from BatchRecord import BatchRecord
from BatchConstants import BatchDataTotalLength
from BatchProcessingExceptions import BatchRecordException


class ABatchRecordShould(TestCase):

    def __init__(self, test_name):
        TestCase.__init__(self, test_name)
        self.br = BatchRecord(BatchDataTotalLength * " ")

    def test_batch_record_raises(self):
        test = " "
        self.assertRaises(BatchRecordException, BatchRecord, test)

    def test_zero_contracts(self):
        self.assertEquals(0, self.br.contracts)

    def test_is_last_record(self):
        pass

if __name__ == '__main__':
    unittest.main()