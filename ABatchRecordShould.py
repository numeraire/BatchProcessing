__author__ = 'blocke'
from unittest import TestCase
from BatchRecord import BatchRecord
from BatchConstants import BatchDataTotalLength
from BatchConstants import BatchRecordDataType
from BatchProcessingExceptions import BatchRecordInvalidDataTypeException, BatchRecordInvalidRecordLength
from BatchProcessingExceptions import BatchRecordLastRecordException


class ABatchRecordShould(TestCase):

    def __init__(self, test_name):
        TestCase.__init__(self, test_name)
        self.br = BatchRecord(BatchRecordDataType + ((BatchDataTotalLength - len(BatchRecordDataType)) * "*"))

    def test_batch_record_invalid_length(self):
        test = " "
        self.assertRaises(BatchRecordInvalidRecordLength, BatchRecord, test)

    def test_zero_contracts(self):
        self.assertEquals(0, self.br.contracts)

    def test_batch_record_is_not_data_type(self):
        test = "I2" + ((BatchDataTotalLength - len(BatchRecordDataType)) * "*")
        self.assertRaises(BatchRecordInvalidDataTypeException, BatchRecord, test)

    def test_batch_record_is_last_record(self):
        test = BatchRecordDataType + ((BatchDataTotalLength - len(BatchRecordDataType)) * "9")
        self.assertRaises(BatchRecordLastRecordException, BatchRecord, test)

#if __name__ == '__main__':
#    main()