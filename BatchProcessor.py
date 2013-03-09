from BatchProcessingExceptions import BatchRecordInvalidDataTypeException, BatchRecordLastRecordException
from BatchRecord import BatchRecord

__author__ = 'blocke'

def main():

    f = open("C:\\Users\\blocke\\Data\\BatchData\\smd_batch_MDDS_fut.out", 'r')

    for line in f:

        try:
            br = BatchRecord(line[16:-1])
        except BatchRecordInvalidDataTypeException as exc:
            pass #print exc.message
        except BatchRecordLastRecordException:
            pass

    f.close()

if __name__ == '__main__':
    main()
