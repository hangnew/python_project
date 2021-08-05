import requests
from bs4 import BeautifulSoup
targetsite = "https://music.bugs.co.kr/chart"

# doc = requests.get(targetsite)
# print(doc) # <Response[200]> : 정상 접속된 것
#
# html = doc.text
# # print(html)
#
# soup = BeautifulSoup(html, 'html.parser') #html 타입의 text파일, html로 parsing
# # print(soup)
# # 3가지가 있지만 html.parser를 사용하자 (궁금하면 검색)
#
# titles = soup.findAll('p', {'class':'title'})
# # print(titles)
#
# for title in titles:
#     print(title.text.strip())

doc = requests.get(targetsite)
print(doc) # <Response[200]> : 정상 접속된 것

html = doc.text
# print(html)

soup = BeautifulSoup(html, 'html.parser') #html 소스가 들어있는 text파일, html로 parsing
# print(soup)
# 3가지가 있지만 html.parser를 사용하자 (궁금하면 검색)

artists = soup.findAll('p', {'class':'artist'})
# print(artists)

for artist in artists:
    print(artist.text.strip().split("\n")[0])
    print('*******************')
#split("문장을 끊을 조건")