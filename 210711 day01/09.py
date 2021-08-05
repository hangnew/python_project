deposit = int(input('1년 만기 정기 예금을 얼마나 예치하시겠습니까? '))
print('원금이 ' + str(deposit) + '이시군요!')

interest = int(deposit * 0.1)
print('이자는 ' + str(interest) + '입니다.')

total_Amount = deposit + interest
print('원리합계는 ' + str(total_Amount) + '입니다.')