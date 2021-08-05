# food = ['아이스크림', '아이스아메리카노', '생수']
# print(food[0])
# print(food[1])
# print(food[2])
#
# for i in range(0, len(food)):
#     print(food[i])
#
# for x in food:
#     print(x)

# 오늘 끝나고 나서 할 일 5가지를 목록으로 만들어 보세요
# 2가지 방식으로 프린트
# todo_list = ['자기', '먹기', '눕기', '씻기', '놀기']
# for i in range(0, len(todo_list)):
#     print(todo_list[i], end=' ')
# print()
# for x in todo_list:
#     print(x, end=' ')

# hobby = []
# hobby.append('코딩')
# print('개수>> ', len(hobby))
# hobby.append('등산')
# print('개수>> ', len(hobby))
#
# for _ in range(3):
#     data = input('당신의 새로운 취미는>> ')
#     hobby.append(data)
# print('개수>> ', len(hobby))
#
# for x in hobby:
#     print(x, end=' ')

# a = ['AB', 10, False]
# x = a[1]
# print(x)
# a[1] = 'Test'
# print(a[1])
# y = a[-1]
# print(y)

# numbers = range(3)
# for x in numbers:
#     print(x, end=' ')
# print()
# numbers2 = range(3, 6)
# for x in numbers2:
#     print(x, end=' ')
# print()
# numbers3 = range(2, 11, 2)
# for x in numbers3:
#     print(x, end=' ')
# print()

# for i in range(10):
#     print('Hello')

# food = []
# for i in range(3):
#     food_input = input('입력입력>> ')
#     food.append(food_input)
# print(food[1])
# print(food[0:2])
# print(food[1:3])
# food[0] = '라면'
# for x in food:
#     print(x, end=' ')

# month = int(input('몇월? '))
# if 3 <= month <= 5:
#     print('봄')
# elif 6 <= month <= 8:
#     print('여름')
# elif 9 <= month <= 11:
#     print('가을')
# else:
#     print('겨울')

# target = 55
# count = 0
# while True:
#     usr = int(input('숫자 입력>> '))
#     count = count + 1
#     if usr == target:
#         print('정답')
#         print(count)
#         break
#     elif usr < target:
#         print('up')
#     else:
#         print('down')

# int1 = int(input('첫번째 숫자 입력: '))
# int2 = int(input('두번째 숫자 입력: '))
# subst = abs(int1 - int2) - 1
# sum = int1 + int2
# avg = (int1 + int2) / 2
# print('끝 사이의 개수:', subst)
# print('두 수의 합:', sum)
# print('두 수의 평균:', avg)

# figure = ['김연아', '나몰라', '김상화', '모태범']
# del figure[1]
# figure[-1] = '모모범'
# for x in figure:
#     print(x)

# pyo = [0, 0, 0]
# while True:
#     vote = int(input('인기투표 : 1)레드벨벳 2)트와이스 3)오마이걸 0)종료  '))
#     if vote == 0:
#         print('투표를 종료합니다.')
#         print('레드벨벳 득표: ' + str(pyo[0]) + '표')
#         print('트와이스 득표: ' + str(pyo[1]) + '표')
#         print('오마이걸 득표: ' + str(pyo[-1]) + '표')
#         break
#     elif vote == 1:
#         pyo[0] = pyo[0] + 1
#         print('레드벨벳')
#     elif vote == 2:
#         pyo[1] = pyo[1] + 1
#     else:
#         pyo[-1] = pyo[-1] + 1

# 안전성 점수 (30%) : 100 		=>	100 * 0.3 = 30
# 속도 점수 (50%) : 80			=>	80 * 0.5 = 40
# 연비 점수 (20%) : 60			=>	60 * 0.2 = 12
# 출력 : 82점 우수입니다
# 90점 이상: 최우수, 80점 이상: 우수, 70점 이상: 보통, 그것도 아니면: 미달

# safety = int(input('안전성 점수: ')) * 0.3
# speed = int(input('속도 점수: ')) * 0.5
# oil = int(input('연비 점수: ')) * 0.2
# total = int(safety + speed + oil)
# if total >= 90:
#     print(str(total) + '점 최우수입니다.')
# elif total >= 80:
#     print(str(total) + '점 우수입니다.')
# elif total >= 70:
#     print(str(total) + '점 보통입니다.')
# else:
#     print(str(total) + '점 미달입니다.')

# id = input('id>> ')
# name = input('이름>> ')
# print('아이디가 ' + id + '인 ' + name + '님이 로그인되었습니다.')

# num1 = int(input('숫자1: '))
# num2 = int(input('숫자2: '))
# print('두 수의 합은', num1 + num2)
# print('두 수의 차는', num1 - num2)
# print('두 수의 곱은', num1 * num2)
# print('두 수의 나눗셈은', num1 / num2)
# print('나머지는', num1 % num2)

# name = input('이름>> ')
# age = int(input('나이>> '))
# age_10 = age + 10
# print(name + '님의 10년 후의 나이는 ' + str(age_10) + '세입니다.')

# money = int(input('엄마 용돈 주세요: '))
# if money > 10000:
#     print('엄마 너무 용돈이 많아요.')
# else:
#     print('엄마 너무 용돈이 적어요.')

# num = int(input('숫자 입력>> '))
# if num % 2 == 0:
#     print('짝수')
# else:
#     print('홀수')

# goal = int(input('실적을 입력하세요>> '))
# bonus = int(goal * 0.2)
# if goal >= 1000:
#     print('축하합니다. 실적을 달성하셨습니다!')
#     print('당신의 이번달 보너스는 ' + str(bonus) + '만원입니다.')
# else:
#     print('더 열심히 하세요.')

# name = input('미사일 이름은: ')
# start = int(input('미사일 시작값은: '))
# move = float(input('미사일 움직이는 값은: '))
# print(name + '미사일이 ' + str(start+move) + '로 이동되었습니다.')

# money = int(input('받은 돈: '))
# cost = int(input('상품의 총액: '))
# tax = int(cost * 0.1)
# change = money - cost
# print('부가세: ' + str(tax))
# print('잔돈: ' + str(change))

# for i in range(10):
#     print('*')

# for i in range(20):
#     print(i + 1)
#
# for i in range(20):
#     print(i + 1, end=' ')

# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)

# count = 0
# for i in range(1, 1001):
#     if i % 3 == 0:
#         count = count + 1
# print(count)

# food = []
# while True:
#     want = input('먹고 싶은 음식 입력 (종료:x): ')
#     if want == 'x':
#         print('입력을 종료합니다')
#         for x in food:
#             print(x, end=' ')
#         break
#     else:
#         food.append(want)

# food = ['고구마', '감자', '양파', '당근', '파']
# for x in food:
#     print(x, end=' ')
# print()
# print(food[0], food[-1])
# print(food[2])
# print(food[2:5])

# places = ['여의도', '신촌', '강남', '속초', '제주도']
# for x in places:
#     print(x, end=' ')
# print()
# del places[2]
# for x in places:
#     print(x, end=' ')
# print()
# places[-1] = '제주시'
# for x in places:
#     print(x, end=' ')
# print()
# for i in range(len(places)):
#     print(str(i+1) + '위: ' + places[i])

# names = ('김', '이', '박', '정', '최')
# for x in names:
#     # print(x, end=' ')

# person = ('홍길동', 100, 'mega')
# print(person)
# person2 = list(person)
# person2[0] = '김길동'
# print(person2)
#
# person3 = tuple(person2)
# print(type(person3))

# food = {'커피', '커피', '라면', '우유', '라면'}
# food2 = set()
# food2.add('라떼')
# print(food)
# print(food2)
# print(food[0])

# me = dict()
# me['name'] = 'hong'
# me['age'] = 100
# me['company'] = 'mega'
# print(me)
#
# you = {'name': 'kim', 'age': 200, 'company': 'kg'}
# print(you)
#
# us = dict(name='park', age=300, company='wework')
# print(us)

# apply1 = {'id': 100, 'subject': 'python', 'room': '708', 'fee': 2000}
# apply2 = {'id': 100, 'subject': 'java', 'room': '709', 'fee': 3000}
# apply3 = {'id': 200, 'subject': 'eclipse', 'room': '709', 'fee': 5000}
