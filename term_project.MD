현재 국내 음원의 순위를 알아보기 위해서는 음원차트 사이트인 멜론, 벅스, 지니 등의 홈페이지에 들어가 확인을 하는 절차를 거쳐야 한다. 그런데 이 때 각 사이트 별로 음원 의 순위를 산출해 내는 기준이 조금씩 다르므로 순위에 차이가 생기게 되는데, 사이트 별로 달라지는 음원의 종합적 순위가 궁금한 이용자에게 한눈에 순위비교를 할 수 있는 정보를 제공하고 싶었다. 
 각 음원사이트로부터 정보를 추출해오기 위해서 먼저 리퀘스트 모듈을 임포트하고, 웹의정보를 utf8으로 인코딩하여 불러왔다. 그렇게까지만 하고 불러온 정보를 출력해보니, 원하는 내용을 포함한 해당 사이트의 모든 정보가 나타났다. 문제는 그 많은 정보들 중 음원순위 상위 열개만 뽑아내는 방법이 미지수라는 것이었다. 처음에는 1위 곡명부터 10위 곡명까지를 find로 찾아와 슬라이싱하는 방법을 이용하려했다. 하지만 그렇게 되니 그 사이에 불필요한 정보가 많이 껴있어 그것들을 제거하는데 수고로움이 들 것 같았다. 그래서 인터넷 서칭을 통해 많은 양의 정보가 저장되어있는 사이트에서 데이터를 끌어올 때에는 beautifulsoup을 이용하는 것이 유용하다는 사실을 알게 되었다. 크롬의 개발자도구를 이용해 곡명과 아티스트명이 저장되어있는 위치의 태그를 알아냈고, 그 경로를 beautifulsoup를 찾아 긁어오자 같은 경로에 저장되어있는 정보들이 모두 출력되었다. 그리고 그것들은 내가 예상했던 바와 같이 노래와 음악가의 이름이었다. 그러나 여전히 사이에 원하지 않는 정보들이 섞여있었다. 이를 제거하기 위해 re모듈을 이용하여 <>사이의 정보를 모두 없애는 공식을 입력했다. 마지막으로 
멜론이외의 사이트로는 지니뮤직을 사용했다. 멜론과 같은 방식으로 beautifulsoup모듈을 이용하여 정보를 뽑아내려했다. 그런데  그렇게했더니 정보가깔끔하게 출력이되지 않았고, .text를 붙이자 이것이 해결됨을 얼마 후에 알아냈다.  그렇게 각각의 사이트에서 상위 10개 음원의 곡명과 아티스트명을 뽑아왔고, 이것을 비교하기 편한 형태로 보이게 하는 방법만을 강구하면 되었다. 1-10순위를 차례로 출력하는 것보다, 각 순위에 해당하는 정보를 두개씩 나란히 보이는게 더 편리할 것이라는 생각을 했고, for 반복문을 1부터10까지의 범위를 잡아 정보를 출력하면 되겠다는 결론에 이르렀다.
그리하여 다음과 같은 결과를 얻을 수 있었고 성공적으로 원하는 프로젝트를 제작하게 되었다 .


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
