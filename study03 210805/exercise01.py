# (51/52일차 내용)
# https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1
# 알라딘 베스트셀러 1위부터 50위까지 책 제목과 가격을 crawling하여 데이터베이스에 저장해보세요.
# db.py : pymysql 임포트 > create 메서드
# 메인py : 리퀘스트/뷰티풀숲/db.py 임포트 > 크롤링 > db.create(data) 호출

import requests
from bs4 import BeautifulSoup
import exercise01_db as db

url = "https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1"
doc = requests.get(url).text
soup = BeautifulSoup(doc, 'html.parser')
# print(soup)

titles = soup.findAll("a", {"class": "bo3"})
# print(titles)
title_list = []
for x in range(len(titles)):
    title_list.append(titles[x].text)
print(title_list)

prices = soup.findAll("span", {"class": "ss_p2"})
print(prices)
price_list = []
for x in range(len(prices)):
    price_list.append(prices[x].text)
print(price_list)

title_list2 = tuple(title_list)
price_list2 = tuple(price_list)
total = list(zip(title_list2, price_list2))
print(total)

db.create(total)
