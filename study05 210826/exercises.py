# "textfile.txt"의 파일명으로 "글자를 파일에 쓰세요"라고 저장하고,
# 발생할 수 있는 IOError를 예외처리 후에 "파일을 찾을 수 없습니다."라고 출력하시오.
# 만약 예외가 발생하지 않는다면 "파일을 생성했습니다." 라고 출력하시오.
# try:
#     f = open("textfile.txt", 'w')
#     f.write('글자를 파일에 쓰세요.')
# except IOError:
#     print('파일을 찾을 수 없습니다.')
# else:
#     print('파일을 생성했습니다.')
# finally:
#     f.close()






# 가위바위보 게임 만들기
# random 모듈을 사용해 베타고라는 가위바위보 게임을 만들어 보세요.
# import random as r
# def betago(rsp):
#     ai = r.randint(1, 3)
#     # 1: 가위, 2: 바위, 3: 보
#     if ai == 1:
#         if rsp == '가위':
#             print('비김')
#         elif rsp == '바위':
#             print('이김')
#         elif rsp == '보':
#             print('짐')
#         else:
#             print('잘못냄')
#     elif ai == 2:
#         if rsp == '가위':
#             print('짐')
#         elif rsp == '바위':
#             print('비김')
#         elif rsp == '보':
#             print('이김')
#         else:
#             print('잘못냄')
#     else:
#         if rsp == '가위':
#             print('이김')
#         elif rsp == '바위':
#             print('짐')
#         elif rsp == '보':
#             print('비김')
#         else:
#             print('잘못냄')
#
# betago('가위')





# 리스트넣어서 랜덤추첨하는 함수 만들기 (중복x)
# member = ["이준규", "변승원", "오주현", "전혜윤"]
# print(ran(member, 2))
# => ['변승원', '전혜윤']
# import random as r
# member = ['이준규', '변승원', '오주현', '전혜윤']
# def ran(a, b):
#     c = []
#     for x in range(b):
#         x = r.randint(0, len(a) - 1)
#         c.append(a[x])
#     return c
# print(ran(member, 2))





# 계산기 만들기 , 나누기0 입력시 예외처리(ZeroDivisionError)
# class Calculator:
#     def __init__(self):
#         self.result = 0
#
#     def plus(self, x):
#         self.result += x
#
#     def minus(self, x):
#         self.result -= x
#
#     def times(self, x):
#         self.result * x
#
#     def sub(self, x):
#         try: self.result /= x
#         except ZeroDivisionError: pass
#
# cal = Calculator()
# cal.plus(8)
# cal.sub(0)
# cal.sub(2)
# print(cal.result)






# #1줄로 코딩하기
# #입력 리스트: [1,-5,3,-4,2,-3,0,-2,-1]
# # 1) 리스트의 각 항목에 3을 더해서 리스트로 출력해보세요
# # 출력:[4, -2, 6, -1, 5, 0, 3, 1, 2]
# # 2) 리스트의 각 항목 중 0보다 큰 항목만 리스트로 출력해보세요
# # 출력:[1, 3, 2]
# # 3) 리스트를 정렬하여 출력해보세요
# # 출력: [-5, -4, -3, -2, -1, 0, 1, 2, 3]
# # 1+2+3) 하기 리스트의 각 항목에 3을 더해서 0보다 큰 항목만 리스트로 정렬하여 출력해보세요
# # 출력: [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: x + 3, [1, -5, 3, -4, 2, -3, 0, -2, -1])))
print(list(filter(lambda x: x > 0, [1, -5, 3, -4, 2, -3, 0, -2, -1])))
print(sorted([1, -5, 3, -4, 2, -3, 0, -2, -1]))
print(sorted(filter(lambda x: x > 0, map(lambda x: x+3, [1, -5, 3, -4, 2, -3, 0, -2, -1]))))
