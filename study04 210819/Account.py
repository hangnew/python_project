class Account:
    def __init__(self, name, account, amount):
        self.name = name
        self.account = account
        self.amount = amount

class AccountNormal(Account):
    RATE = 0.01
    def n(self):
        print(self.amount + self.amount * self.RATE, '원')

class AccountVip(Account):
    RATE = 0.1
    def v(self):
        print(self.amount + self.amount * self.RATE, '원')

if __name__ == "__main__":
    print("이 파일은 모듈입니다. 다른 파일에서 import하여 사용해주세요.")
