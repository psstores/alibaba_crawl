#encoding=utf-8
import urllib2,urllib
import time
import json
import csv
import codecs 
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
##订单
url_start='http://shop.mogujie.com/trade/item_detail/orderlist?itemId=16p1o44&page=1'
url='http://shop.mogujie.com/trade/item_detail/orderlist?itemId=16p1o44&page='
f=urllib2.urlopen(url_start)
con=f.read()
##print type(con)
s=json.loads(con,encoding='utf-8')
f.close()

##
def get_last_page(url):
    url=url
    f=urllib2.urlopen(url)
    con=f.read()
    s=json.loads(con,encoding='utf-8')
    f.close()
    html=s['result']['html']
    soup=BeautifulSoup(html,'html.parser',from_encoding='utf-8')
    page_data=soup.find_all('div',{'class':'pagination'})  
    last_page=page_data[0].find_all('a')[5].text
    return last_page

def write_to_csv(html,page):
    soup=BeautifulSoup(html,'html.parser',from_encoding='utf-8')
    g_data=soup.find_all('tr')
    k=0
##    print page
    for item in g_data:
        try:
            dd=item.find_all('td')
            user=(dd[0].text).strip()
            time=dd[1].text
            size=(dd[2].text).split(' ')[1]
            color=(dd[2].text).split(' ')[0]
            page1=u'第'+str(page)+u'页'
            d=[page1,user,color,size,time]
            
            with codecs.open('sale.csv','a+','utf-8') as fd:
                                       fd.write('\xEF\xBB\xBF')
                                       write=csv.writer(fd,dialect='excel')
                                       write.writerow(d)
                                       fd.close()
                                       print page1
        except:
            pass
    
   

def get_content(url,last_page):
    for page in range(1,last_page+1):
        url1=url+str(page)
        print url1
        f=urllib2.urlopen(url1)
        con=f.read()
        ##print type(con)
        s=json.loads(con,encoding='utf-8')
        f.close()
        html=s['result']['html']
        write_to_csv(html,page)
        
        print page
        


if __name__ == '__main__':
   
    last_page=get_last_page(url=url_start)
    last_page=int(last_page)
    print last_page
    get_content(url=url,last_page=last_page)
    



