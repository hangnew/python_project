import requests
from bs4 import BeautifulSoup
import mysql02_db as db

url = "https://finance.naver.com/sise/lastsearch2.nhn"
doc = requests.get(url)
content = doc.text
soup = BeautifulSoup(content, 'html.parser')
# print(soup)

titles = soup.findAll("a", {"class": "tltle"})
# print(len(titles))
# print(type(titles))

title_list = []
for x in range(len(titles)):
    title_list.append(titles[x].text)
# print(len(title_list))
# print(type(title_list))
# print(title_list)

numbers = soup.findAll("td", {"class": "number"})
# print(len(numbers))
# # print(numbers)
# now = numbers[1].text
# print('현재가:', now)
# high = numbers[6].text
# print('상한가:', high)
# low = numbers[7].text
# print('하한가:', low)

now_list = []
for x in range(1, len(numbers), 10):
    data = numbers[x].text
    now_list.append(data)

high_list = []
for x in range(6, len(numbers), 10):
    data = numbers[x].text
    high_list.append(data)

low_list = []
for x in range(7, len(numbers), 10):
    data = numbers[x].text
    low_list.append(data)

# print(title_list)
# print(now_list)
# print(high_list)
# print(low_list)

title_list2 = tuple(title_list)
now_list2 = tuple(now_list)
high_list2 = tuple(high_list)
low_list2 = tuple(low_list)

total_list = list(zip(title_list2, now_list2, high_list2, low_list2))
print(total_list)
print(len(total_list))
print(type(total_list))

total = tuple(total_list)
print(type(total))
print(total)

db.create(total)
