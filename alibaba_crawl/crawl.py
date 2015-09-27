#encoding=utf-8
import csv
import sys
import MySQLdb
reload(sys)
sys.setdefaultencoding( "utf-8")
import codecs
import subprocess
import chardet
import time
from bs4 import BeautifulSoup
def getDom(page):
            cmd=r'casperjs E:\test\a\casper1.js'+' --page='+page
            print "cmd",cmd
            stdout,stderr=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
            print stderr
            fp=open('html.txt','w')
            print u'第'+page+u'页'
            fp=open('html.txt','w')
            
            soup=BeautifulSoup(stdout,'html.parser',from_encoding="gb18030")
            g_data=soup.find_all("li",{"class":"sm-offer-item sw-dpl-offer-item "})
            
            print len(g_data)
            fp.write(stdout)
            fp.close()
            ##变量写入字典
            for item in g_data:
                     try:
                            com=(item.find_all('a',{'class':'sm-offer-companyName sw-dpl-offer-companyName '})[0].text).strip()
                     except:
                            com=(item.find_all('a',{'class':'sm-offer-companyName sw-dpl-offer-companyName sm-offer-name-short'})[0].text).strip()
                            
                    ##销量
                     try:
                            sale=(item.find_all('span',{'class':'sm-offer-trade sw-dpl-offer-trade'})[0].text).strip()
                     except:
                            sale= '0'
                    ##价格
                    #print item.find_all('span',{'class','sm-offer-priceNum sw-dpl-offer-priceNum'})[0].text
                    ##标题
                     title=(item.find_all('div',{'class':'sm-offer-title sw-dpl-offer-title'})[0].text).strip()
                    ##诚信通年份
                     year=(item.find_all('span',{'class':'sm-offer-companyTag sw-dpl-offer-companyTag'})[0].text).strip()
                    ##公司位置
                     #location=(item.find_all('div',{'class':'sm-offer-location'})[0].text).strip()
                    ##Link
                     link=item.find_all('a',{'class':'sm-offer-photoLink sw-dpl-offer-photoLink'})[0].get('href')
                     d=[com,sale,title,year,link]
                     #write to csv
                     with codecs.open('test.csv','a+','utf-8') as fd:
                           fd.write('\xEF\xBB\xBF')
                           write=csv.writer(fd,dialect='excel')
                           write.writerow(d)
                           fd.close()
                     #write to mysql
        ##             conn=MySQLdb.connect(host='localhost',user='Jason',passwd='520205',db='jason',charset='utf8')
        ##             cursor=conn.cursor()
        ##             sql='insert into ali(com,deal,title,year,url) values(%s,%s,%s,%s,%s)'
        ##             param=d
        ##             n=cursor.execute(sql,param)
        ##             conn.commit()
        ##             print 'insert',n

##            cursor.close()
##            conn.close()
            print u'delay 2 second'
            time.sleep(1)
            
for page in range(1,15):
    page=str(page)                               
    getDom(page)  
    
                  
