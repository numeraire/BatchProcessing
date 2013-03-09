__author__ = 'blocke'
from BatchProcessingExceptions import BatchRecordInvalidRecordLength, BatchRecordInvalidDataTypeException, \
    BatchRecordLastRecordException
from BatchConstants import BatchDataTotalLength, BatchRecordDataType, BatchRecordLastRecord


class BatchRecord(object):

    def __init__(self, record):

        if record[:2] != BatchRecordDataType:
            msg = "Invalid batch record data type (%s)" % record[:2]
            raise BatchRecordInvalidDataTypeException(msg)

        if len(record) != BatchDataTotalLength:
            msg = "Invalid batch record length (%s)" % str(len(record))
            raise BatchRecordInvalidRecordLength(msg)

        if record[18:30] == BatchRecordLastRecord:
            raise BatchRecordLastRecordException("Last Record")

        self.data_type = record[:2]
        self.issue_count = record[5:10]
        self.trading_date_YYYY = record[10:14]
        self.trading_date_MM = record[14:16]
        self.trading_date_DD = record[16:18]
        self.issue_code = record[18:30]
        self.issue_seq_no = record[30:36]
        self.issue_code_abbrev = record[46:55]
        self.spread_type = record[355:357]