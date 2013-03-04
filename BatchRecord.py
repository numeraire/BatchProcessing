__author__ = 'blocke'

class BatchRecord(object):

    def __init__(self,record):
        self.ISIN = record[:1]

    def testmethod(self):
        print "a"

