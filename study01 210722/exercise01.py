# 1) 자동차 검사
# 안전성 점수 (30%) : 100
# 속도 점수 (50%) : 80
# 연비 점수 (20%) : 60
# (출력내용) 82점 우수입니다
# (90점 이상: 최우수, 80점 이상: 우수, 70점 이상: 보통, 그것도 아니면: 미달)
# safety = int(input("안전성 점수 (30%): ")) * 0.3
# speed = int(input("속도 점수 (50%): ")) * 0.5
# fuel = int(input("연비 점수 (20%): ")) * 0.2
# total = int(safety + speed + fuel)
# if total >= 90:
#     print(str(total) + "점 최우수입니다.")
# elif total >= 80:
#     print(str(total) + "점 우수입니다.")
# elif total >= 70:
#     print(str(total) + "점 우수입니다.")
# else:
#     print(str(total) + "점 미달입니다.")

# 2) 투표 프로그램
# 리스트와 while을 이용해서 투표 프로그램을 만들어 보세요
# 사용자가 종료할 때까지 반복됩니다. 아래같이 출력되게 해보세요
# (출력내용)
# 인기투표 : 1) 레드벨벳 2) 트와이스 3) 오마이걸 4) 종료		1(입력)
# 레드벨벳 1표 획득!
# 인기투표 : 1) 레드벨벳 2) 트와이스 3) 오마이걸 4) 종료		3(입력)
# 오마이걸 1표 획득!
# 인기투표 : 1) 레드벨벳 2) 트와이스 3) 오마이걸 4) 종료		4(입력)
# 투표를 종료합니다.
# 레드벨벳 득표수 : 1표
# 트와이스 득표수 : 0표
# 오마이걸 득표수 : 1표


# 1) 다음 문장의 글자를 거꾸로 출력해보세요 (문자열 인덱싱과 for문 이용)
# "Welcome to Python World!"
# => (출력내용) "!dlroW nohtyP ot emocleW"
# words = "Welcome to Python World!"
# for i in range(len(words)):
#     print(words[-1-i], end="")
# text = "Welcome to Python World!"
# new = ""
# for i in range(1, len(text) + 1):
#     print(text[-i], end="")
# print("")
#
# for i in range(1, len(text) + 1):
#     new = new + text[-i]
# print(new)

# 2) 다음 딕셔너리에서 value값이 0인 key의 집합(리스트)을 만들어 출력하시오
# dic = {'a':0, 'b':0,'c':2,'d':1,'e':0}
# => (출력내용) ['a','b','e']
dic = {'a': 0, 'b': 0, 'c': 2, 'd': 1, 'e': 0}
keys = []
for i in dic:
    if dic[i] == 0:
        keys.append(i)
print(keys)

# 1)id와 pw가 각각 root/1234일 경우 로그인하는 함수를 만들고
# id,pw입력받아서 함수사용하여 로그인 성공/실패 출력하기
# id: 입력
# pw: 입력
# 함수(id,pw)
# =>(출력내용)로그인성공
# id = "root"
# pw = "1234"
# id2 = input("id: ")
# pw2 = input("pw: ")
# if id == id2 and pw == pw2:
#     print("로그인 성공")
# else:
#     print("로그인 실패")
# def login(id, pw):
#     result = "로그인 실패"
#     if id == "root" and pw == "1234":
#         result = "로그인 성공"
#     print(result)
#
# id = input("id입력: ")
# pw = input("pw입력: ")
#
# login(id, pw)

# 2)주민등록번호 입력받아서 남자인지 여자인지 구분하는 함수,
# 나이계산하는 함수 각각 만들어서 출력하기
# ssn:입력
# 성별함수(ssn)
# 나이함수(ssn)
# =>(출력내용) 성별, 나이
# def gender(ssn):
#     result = "남자"
#     if ssn[6] == "2":
#         result = "여자"
#     print(result)
#
# def age(ssn):
#     result = 0
#     if 22-int(ssn[0:2]) >= 1:
#         result = 22-int(ssn[0:2])
#     else:
#         result = 122-int(ssn[0:2])
#     print("나이는 " + str(result) + "살 입니다.")
#
# ssn = input("주민등록번호 입력: ")
# gender(ssn)
# age(ssn)