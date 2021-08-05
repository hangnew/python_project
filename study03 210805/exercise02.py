# (5일차 내용)
# Triangle이라는 클래스를 만들어 삼각형의 세 각을 입력받아 객체 생성 후
# 메서드를 이용하여 삼각형인지 아닌지, 맞다면 정삼각형인지, 총 몇 개의 삼각형이 만들어졌는지 알려주세요.
# (예: 입력 90, 30, 60 >> tri1.check_angles() >> 출력: 삼각형입니다.)
# (예: 입력 60, 60, 60 >> tri2.check_angles() >> 출력: 정삼각형입니다.)
# (예: 입력 90, 90, 30 >> tri3.check_angles() >> 출력: 삼각형이 아닙니다.)
# (예: Triangle.count >> 삼각형이 총 3개 만들어졌습니다.)

class Triangle:
    count = 0
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = int(angle1)
        self.angle2 = int(angle2)
        self.angle3 = int(angle3)
        Triangle.count += 1

    def check_angles(self):
        result = '삼각형이 아닙니다'
        if self.angle1 + self.angle2 + self.angle3 == 180:
            result = '삼각형입니다'
            if self.angle1 == self.angle2 == self.angle3 == 60:
                result = '정삼각형입니다'
        return result

tri1 = Triangle(input('각1: '), input('각2: '), input('각3: '))
print(tri1.check_angles())
tri2 = Triangle(input('각1: '), input('각2: '), input('각3: '))
print(tri2.check_angles())
tri3 = Triangle(input('각1: '), input('각2: '), input('각3: '))
print(tri3.check_angles())
print('삼각형이 총 ' + str(Triangle.count) + '개 만들어졌습니다.')