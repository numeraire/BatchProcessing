__author__ = 'blocke'


class BatchRecordException(Exception):
    pass


class BatchRecordInvalidDataTypeException(BatchRecordException):
    pass


class BatchRecordInvalidRecordLength(BatchRecordException):
    pass


class BatchRecordLastRecordException(BatchRecordException):
    pass