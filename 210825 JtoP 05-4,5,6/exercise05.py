# 1. Calculator 클래스를 상속하는 UpgradeCalculator를 만들고
# 값을 뺄 수 있는 minus 메서드를 추가해 보자.
# class Calculator:
#     def __init__(self):
#         self.value = 0
#
#     def add(self, val):
#         self.value += val

# class UpgradeCalculator(Calculator):
#     def minus(self, val):
#         self.value -= val
#
# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)
# print(cal.value)

# 2. 객체 변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어 보자
# class MaxLimitCalculator(Calculator):
#     def add(self, val):
#         self.value += val
#         if self.value > 100:
#             self.value = 100
#
# cal = MaxLimitCalculator()
# cal.add(50)
# cal.add(60)
# print(cal.value)

# 4. filter와 lambda를 사용하여 리스트 [ 1, -2, 3, -5, 8, -3 ] 에서 음수를 모두 제거해 보자.
# print(list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3])))

# 6. map과 lambda를 이용하여 [1, 2, 3, 4] 리스트의 각 요솟값에 3이 곱해진 리스트 [3, 6, 9, 12]를 만들어 보자.
# print(list(map(lambda x: x * 3, [1, 2, 3, 4])))

# 7. [-8, 2, 7, 5, -3, 5, 0, 1] 최대값과 최소값의 합을 구해 보자
# l = [-8, 2, 7, 5, -3, 5, 0, 1]
# print(max(l) + min(l))

# 8. 17 / 3 의 결과값 5.666666667을 소수점 4자리까지만 반올림하여 표시해 보자.
# print(round(17 / 3, 4))

# 13. random 모듈을 사용하여 로또 번호 (1~45 사이의 숫자 6개)를 생성해 보자 (단 중복된 숫자가 있으면 안 됨)
# import random as r
# n = set([])
# while len(n) < 7:
#     n.add(r.randint(1, 45))
# print(n)
