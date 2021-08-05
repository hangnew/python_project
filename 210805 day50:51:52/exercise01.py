class Day:
    def __init__(self, subj, hour, locate):
        self.subj = subj
        self.hour = hour
        self.locate = locate

    def study(self):
        result = self.subj + '를 ' + self.hour + '시간 하다'
        return result

    def where(self):
        result = self.locate + '에서 ' + self.subj + '를 하다'
        return result

a = Day('파이썬공부', '10', '강남')
b = Day('자바공부', '11', '신촌')
c = Day('db공부', '12', '종로')

print(a.study())
print(a.where())
print(b.study())
print(b.where())
print(c.study())
print(c.where())