# raise : 강제로 오류를 발생시킨다
class Bird:
    def fly(self):
        raise NotImplementedError

# class Eagle(Bird):
#     pass
#
# eagle = Eagle()
# eagle.fly()

# 메서드 오버라이딩
class Eagle(Bird):
    def fly(self):
        print('very fast')
