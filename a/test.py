# -*- coding: utf-8 -*-
import codecs
import csv
##import sys
##reload(sys)
##sys.setdefaultencoding("utf-8")
d=[u'中车人',u'中车人',u'中车人']
with codecs.open('test.csv','a+','utf-8') as fd:
                               fd.write('\xEF\xBB\xBF')
                               write=csv.writer(fd,dialect='excel')
                               write.writerow(d)
                               fd.close()
