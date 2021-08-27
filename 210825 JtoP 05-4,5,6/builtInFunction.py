# abs(x) : 절대값

# all(x) : 반복 가능한 자료형 x를 입력, x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False

# any(x) : 반복 가능한 자료형 x를 입력, x의 요소 중 하나라도 참이면 True, 모두가 거짓이면 False

# chr(i) : 유니코드 값을 입력받아 해당 문자를 출력 (ord 함수와 반대)

# dir(객체) : 객체가 자체적으로 가지고 있는 변수나 함수 출력

# divmod(a, b) : 숫자 2개 입력, a를 b로 나눈 몫과 나머지가 튜플로 반환 (a // b, a % b)

# enumerate(자료형) : 자료형을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 반환
# for i, name in enumerate(['body', 'foo', 'bar']):
#     print(i, name)

# eval(expression) : 실행 가능한 문자열을 입력 받아 문자열을 실행한 결괏값을 돌려준다

# filter : 첫 번째 인수로 함수 이름, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형
# 두 번째 인수인 자료형 요소가 첫 번째 인수인 함수에 입력되었을 때 참인 것만 걸러 내서 돌려준다
# def positive(l):
#     result = []
#     for i in l:
#         if i > 0:
#             result.append(i)
#     return result
# print(positive([1, -3, 2, 0, -5, 6]))
#
# def positve2(x):
#     return x > 0
# print(list(filter(positve2, [1, -3, 2, 0, -5, 6])))

# hex(x) : 정수 값을 입력받아 16진수로 반환

# id(object) : 객체를 입력받아 객체의 고유 주소 값을 반환

# input : 사용자 입력을 받는 함수

# int(x) : 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 반환

# int(x, radix) : radix 진수로 표현된 문자열 x를 10진수로 변환하여 반환
# print(int('11', 2))
# print(int('1A', 16))

# isinstance(object, class) : 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다
# 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지 판단하여 참이면 True, 거짓이면 False

# len(s) : 입력값 s의 길이를 돌려준다

# list(s) : 반복 가능한 자료형 s를 입력받아 리스트로 만들어 반환

# map(f, iterable) : 함수 f와 반복 가능한 자료형을 입력받는다
# map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려준다
# def two_times(numberlist):
#     result = []
#     for number in numberlist:
#         result.append(number * 2)
#     return result
# print(two_times([1, 2, 3, 4]))
#
# def two_times2(x):
#     return x * 2
# print(list(map(two_times2, [1, 2, 3, 4])))

# max(iterable) : 인수로 반복 가능한 자료형을 입력 받아 그 최댓값을 돌려주는 함수
# print(max([1, 2, 3]))

# min(iterable) : 인수로 반복 가능한 자료형을 입력 받아 그 최소값을 돌려주는 함수
# print(min([1, 2, 3]))

# oct(x) : 정수 형태의 숫자를 8진수 문자열로 반환

# open(filename, [mode]) : "파일 이름"과 "읽기 방법"을 입력받아 파일 객체를 돌려준다.
# w: 쓰기모드, r: 읽기모드, a: 추가모드, b: 바이너리 모드

# ord(c) : 문자의 유니코드 값을 반환 (chr 함수와 반대)

# pow(x, y) : x의 y 제곱한 결과값

# range([start,] stop [,step]) : for문과 함께 쓰이는 함수
# 입력하는 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려준다
# 인수가 하나인 경우 : 0부터 해당 숫자까지 반복
# 인수가 두개인 경우 : 시작 숫자와 끝 숫자
# 인수가 세개인 경우 : 시작 숫자, 끝 숫자, 숫자 사이의 거리
# print(list(range(1, 10, 2)))

# round(number [, ndigits]) : 숫자를 입력받아 반올림, 표시하고 싶은 소수점의 자리수
# print(round(4.6))
# print(round(5.678, 2))

# sorted(iterable) : 입력값을 정렬한 후 리스트로 돌려준다
# 리스트 자료형에도 sort가 있지만, 리스트 객체 자체를 정렬만 할 뿐 정렬된 결과를 돌려주지는 않는다.

# str(object) : 객체를 문자열 형태로 변환

# sum(iterable) : 입력받은 리스트나 튜플의 모든 요소의 합

# tuple(iterable) : 반복 가능한 자료형을 입력 받아 튜플형으로 바꾸어 돌려준다

# type(object) : 입력값의 자료형을 알려준다

# zip(*iterable) : 동일한 개수로 이루어진 자료형을 묶어 주는 역할의 함수
