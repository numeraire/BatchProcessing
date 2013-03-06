__author__ = 'blocke'
from BatchProcessingExceptions import BatchRecordException
from BatchConstants import BatchDataTotalLength


class BatchRecord(object):

    def __init__(self, record):

        if len(record) != BatchDataTotalLength:

            raise BatchRecordException("Invalid batch record length (" + str(len(record)) + ")")

        self.ISIN = record[:1]
        self.contracts = 0
