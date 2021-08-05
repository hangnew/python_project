# 주현 1)  벅스 뮤직 가수 크롤링하기
# https://music.bugs.co.kr/chart
# (여백 없이 가수 이름만 콘솔 창에 출력되도록 진행)
# import requests
# from bs4 import BeautifulSoup
# targetsite = "https://music.bugs.co.kr/chart"
# doc = requests.get(targetsite)
# print(doc) # <Response[200]> : 정상 접속된 것
#
# html = doc.text
# # print(html)
#
# soup = BeautifulSoup(html, 'html.parser') #html 소스가 들어있는 text파일, html로 parsing
# # print(soup)
# # 3가지가 있지만 html.parser를 사용하자 (궁금하면 검색)
#
# artists = soup.findAll('p', {'class':'artist'})
# # print(artists)
#
# for artist in artists:
#     print(artist.text.strip().split("\n")[0])
#     print('*******************')
#split("문장을 끊을 조건")





# 주현 2) 튜플의 데이터를 변경하는 함수(tuple_change)를 만들어보자
# tp = ('복숭아', '딸기', '무화과')
# 정의한 함수를 tp에 적용: tp = tuple_change(tp, 1, '오디')
# tp 출력 결과 >> ('복숭아', '오디', '무화과')

# (바꾸고싶은 리스트, 인덱스, 바뀔 내용)
# def tuple_change(a, b, c):
#     l = list(a)
#     l[b] = c
#     t = tuple(l)
#     print(t)
#
# tp = ('복숭아', '딸기', '무화과')
# tuple_change(tp, 1, '오디')




# 승원 1) '핸드폰번호를 -를 넣어 입력해주세요>> '를 콘솔을 통해 입력을 받고 앞 세자리, 중간 네자리, 끝 네자리를 세개로 분리하시오.
# 그리고 각각 '핸드폰 앞 세자리는 ', '핸드폰 중간 네자리는 ', '핸드폰 끝 네자리는 '을 붙여서 출력하시오.
# first, middle, last = input('핸드폰 번호를 -를 넣어 입력해주세요>> ').split('-')
# print('핸드폰 앞 세 자리는', first)
# print('핸드폰 중간 네 자리는', middle)
# print('핸드폰 네 끝자리는', last)




# 승원 2) 양궁, 사격, 펜싱, 태권도, 레슬링 순으로 올림픽 일정이 잡혀 있습니다.
# 위의 일정 순서대로 콘솔에 입력을 받고 (while문 사용)
# 빈 배열에 넣으고 프린트 하시오.
# 역도가 올림픽 종목에 추가되고 일정이 가장 처음으로 배정되어서 배열 제일 첫번째에 역도를 넣으시오. (콘솔 사용 x)
# olympics = []
# i = 0
# while i < 5:
#     a = input('순서 입력: ')
#     olympics.append(a)
#     i+=1
# print(olympics)
# olympics.insert(0, '역도')
# print(olympics)





# 준규
# https://www.op.gg/ranking/ladder/
# 1. t1 gumayusi가 랭킹 몇윈지 프린트
# import requests
# from bs4 import BeautifulSoup
# site = "https://www.op.gg/ranking/ladder/"
# doc = requests.get(site)
# html = doc.text
# soup = BeautifulSoup(html, 'html.parser')
# top = soup.findAll('a', {'class':'ranking-highest__name'})

# 2. 승률 55%가 넘는 사람 프린트