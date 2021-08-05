# 1. 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자
# def is_odd(num):
#     if num % 2 == 0:
#         result = '이것은 짝수'
#         return result
#     else:
#         result = '이것은 홀수'
#         return result
#
#
# print(is_odd(8))

# 2. 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.
# 단, 입력으로 들어오는 수의 개수는 정해져 있지 않다.
# def get_avg(*args):
#     sum = 0
#     for x in args:
#         sum += x
#     avg = sum / len(args)
#     return avg
#
# print(get_avg(1, 2, 3))
# print(get_avg(2, 4))

# 3. 오류를 수정해 보자
# input1 = input("첫번째 숫자를 입력하세요: ")
# input2 = input("두번째 숫자를 입력하세요: ")
# total = input1 + input2
# print("두 수의 합은 %s 입니다" % total)
# input1 = input("첫번째 숫자를 입력하세요: ")
# input2 = input("첫번째 숫자를 입력하세요: ")
# total = int(input1) + int(input2)
# print("두 수의 합은 %d입니다." % total)

# 5. 오류를 수정해 보자
# f1 = open("test.txt", 'w')
# f1.write("Life is too short")
# f2 = open("test.txt", 'r')
# print(f2.read())

# f1 = open("test.txt", 'w')
# f1.write("Life is too short")
# f1.close()
# f2 = open("test.txt", 'r')
# print(f2.read())
# f2.close()

# with open("test.txt", 'w') as f1:
#     f1.write("life is too short")
# with open("test.txt", 'r') as f2:
#     print(f2.read())

# 6. "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자
# Life is too short
# you need java
with open("test2.txt", 'w') as f:
    f.write("Life is too short\n")
    f.write("you need java\n")
with open("test2.txt", 'r') as f:
    lines1 = f.read()
print(lines1)
replace = lines1.replace("java", "python")
with open("test2.txt", 'w') as f:
    f.write(replace)
with open("test2.txt", 'r') as f:
    print(f.read())
