coffee_Price = input('커피값 입력')
coffee_Count = input('인원수')
sum = int(coffee_Price) * int(coffee_Count)

if sum >= 20000:
    print('2000원을 할인해드립니다.')
    print(sum - 2000, '원 결제하세요')
else:
    print('계산값을 다 지불하셔야합니다')
    print(sum, '원 결제하세요')
