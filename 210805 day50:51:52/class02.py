# 클래스의 상속, 메서드 오버라이딩

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


class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
print(a.add())
print(a.pow())

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
print(a.div())
