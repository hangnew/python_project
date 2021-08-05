# 메서드와 생성자, 객체 변수

class FourCal:
    # 생성자
    def __init__(self, first, second):
        self.first = first
        self.second = second
    # 메서드 첫 번째 매개변수 : self
    # 호출한 객체 자신이 전달된다.

    def setdata(self, first, second):
        # 객체에 생성되는 객체만의 변수를 객체변수라고 부른다.
        self.fisrt = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
# print(type(a))
a.setdata(4, 2)
# print(a.first)
# print(a.second)

b = FourCal()
b.setdata(3, 7)
# 주소값 확인 : id() 함수
print(id(a.first))
print(id(b.first))
