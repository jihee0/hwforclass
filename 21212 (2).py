import requests, re
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}

url1='https://www.melon.com/chart/index.htm'
url2='http://www.genie.co.kr/chart/top200'

r1=requests.get(url1,headers=header)
r2=requests.get(url2,headers=header)
r1.encoding='utf8'
r2.encoding='utf8'


data1=r1.text
data2=r2.text



music1_parse = BeautifulSoup(data1,'html.parser')
music2_parse = BeautifulSoup(data2,'html.parser')

title1 = music1_parse.select('#lst50 > td > div > div > div.ellipsis.rank01 > span > a ')

artist1 = music1_parse.select('#lst50 > td > div > div > div.ellipsis.rank02 > span')

title2 = music2_parse.select('#body-content > div.newest-list > div > table > tbody > tr > td.info > a.title.ellipsis')

artist2 = music2_parse.select('#body-content > div.newest-list > div > table > tbody > tr > td.info > a.artist.ellipsis')

print('<멜론차트/지니차트>')
for i in range(10):
    print(i,'위')
    print(artist1[i].text,'---',title1[i].text)
    artist2[i]=re.sub('<.+?>', '', str(artist2[i]))
    title2[i]=re.sub('<.+?>', '', str(title2[i]))
    title2[i] = title2[i].replace(' ','')
    title2[i] = title2[i].replace('\n','')
    print(artist2[i],'---', title2[i])
    print('\n')


    
    
    
