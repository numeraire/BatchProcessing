__author__ = 'blocke'
from BatchProcessingExceptions import BatchRecordInvalidRecordLength, BatchRecordInvalidDataTypeException, \
    BatchRecordLastRecordException
from BatchConstants import BatchDataTotalLength, BatchRecordDataType, BatchRecordLastRecord


class BatchRecord(object):

    def __init__(self, record):

        if len(record) != BatchDataTotalLength:
            msg = "Invalid batch record length (%s)", str(len(record))
            raise BatchRecordInvalidRecordLength(msg)

        if record[:2] != BatchRecordDataType:
            msg = "Invalid batch record data type (%s)", record[:2]
            raise BatchRecordInvalidDataTypeException(msg)

        if record[18:30] == BatchRecordLastRecord:
            raise BatchRecordLastRecordException("Last Record")

        self.data_type = record[:2]
        self.ISIN = record[:1]
        self.contracts = 0
