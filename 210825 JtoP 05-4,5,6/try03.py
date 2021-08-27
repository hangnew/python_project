# 에외 만들기

# Exception 클래스를 상속받아 에러 클래스를 만든다
# 오류 메시지를 출력했을 때 오류메시지가 보이게 하려면 __str__ 메서드를 구현한다
class MyError(Exception):
    def __str__(self):
        return '혀용되지 않는 별명입니다'

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

# say_nick('천사')
# say_nick('바보')

try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)
