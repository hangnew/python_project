class Account:
    total = 0
    def __init__(self, product, name, money):
        self.product = product
        self.name = name
        self.money = money
        Account.total += money

    def productMoney(self):
        result = self.product + ' 통장에는 ' + str(self.money) + '만원이 들어있어요.'
        return result

    def nameMoney(self):
        result = self.name + '의 통장에는 ' + str(self.money) + '만원이 들어있어요.'
        return result

a = Account('청약저축', '김아무개', 500)
b = Account('내 비상금', '김아무개딸', 30)
c = Account('자유적금', '박아무개', 100)
print(b.productMoney())
print(c.nameMoney())
print('우리 집 전체 예금액은 ' + str(Account.total) + '만원이에요.')
