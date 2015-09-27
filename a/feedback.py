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
##评论
url='http://shop.mogujie.com/trade/item_detail/ratelist?itemId=16obuoe&order=&page='
f=urllib2.urlopen(url)
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
    html=s['result']
    soup=BeautifulSoup(html,'html.parser',from_encoding='utf-8')
    g_data=soup.find_all('li',{"class":"comment_item clearfix "})
    g_data_odd=soup.find_all('li',{"class":"comment_item clearfix odd"})
    page_data=soup.find_all('div',{"class":"pagination"})
    last_page=page_data[0].find_all('a')[6].text
    return last_page
    



def write_to_csv(html):
    soup=BeautifulSoup(html,'html.parser',from_encoding='utf-8')
    g_data=soup.find_all('li',{"class":"comment_item clearfix "})

    soup=BeautifulSoup(html,'html.parser',from_encoding='utf-8')
    g_data_odd=soup.find_all('li',{"class":"comment_item clearfix odd"})

    
    for item in g_data_odd:
        try:
            uname=item.find_all('a',{"class":"uname"})[0].text
        except:
            uname=item.find_all('span',{"class":"uname"})[0].text
        content=(item.find_all('p',{"class":"content"})[0].text).strip()
        time=item.find_all('span',{"class":"fl"})[0].text
        color=item.find_all('span',{"class":"fl"})[1].text
        size=item.find_all('span',{"class":"fl"})[2].text
        d=[uname,content,color,time,size]
        with codecs.open('feedback.csv','a+','utf-8') as fd:
                                   fd.write('\xEF\xBB\xBF')
                                   write=csv.writer(fd,dialect='excel')
                                   write.writerow(d)
                                   fd.close()
    item=None
    d=None
    for item in g_data:
        try:
            uname=item.find_all('a',{"class":"uname"})[0].text
        except:
            uname=item.find_all('span',{"class":"uname"})[0].text
        content=(item.find_all('p',{"class":"content"})[0].text).strip()
        time=item.find_all('span',{"class":"fl"})[0].text
        color=item.find_all('span',{"class":"fl"})[1].text
        size=item.find_all('span',{"class":"fl"})[2].text
        d=[uname,content,color,time,size]
        with codecs.open('feedback.csv','a+','utf-8') as fd:
                                   fd.write('\xEF\xBB\xBF')
                                   write=csv.writer(fd,dialect='excel')
                                   write.writerow(d)
                                   fd.close()

def get_content(url,last_page):
    for page in range(1,last_page+1):
        url1=url+str(page)+'&type=1&emotion=&property=&sort=1&ptp=1.po63RQbx.Oyk4EmIE.162.P0uwA5'
        print url
        f=urllib2.urlopen(url1)
        con=f.read()
        ##print type(con)
        s=json.loads(con,encoding='utf-8')
        f.close()
        html=s['result']
        write_to_csv(html)
        print page


if __name__ == '__main__':
    last_page=get_last_page(url=url)
    last_page=int(last_page)
    print last_page
    get_content(url=url,last_page=last_page)
    



