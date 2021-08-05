class Member:
    total = 0
    count = 0

    def __init__(self, id, pw, level, mileage):
        self.id = id
        self.pw = pw
        self.level = level
        self.mileage = mileage
        Member.total += int(mileage)
        Member.count += 1

    def pwCheck(self, id):
        result = self.id + '의 비밀번호는 ' + self.pw + '입니다.'
        return result

    def levelCheck(self, id):
        result = self.id + '는 ' + self.level + '이고 마일리지는 ' + self.mileage + '입니다.'
        return result

a = Member(input('아이디>> '), input('비밀번호>> '), input('등금>> '), input('마일리지>> '))
b = Member(input('아이디>> '), input('비밀번호>> '), input('등금>> '), input('마일리지>> '))
c = Member(input('아이디>> '), input('비밀번호>> '), input('등금>> '), input('마일리지>> '))
print(a.pwCheck('admin'))
print(b.levelCheck('manager'))
print('총 마일리지는 ' + str(Member.total) + '입니다.')
print('평균 마일리지는 ' + str(int(Member.total / Member.count)) + '입니다.')
