# match 객체의 메서드
# group() : 매치된 문자열을 돌려준다
# start() : 매치된 문자열의 시작 위치를 돌려준다
# end() : 매치된 문자열의 끝 위치를 돌려준다
# span() : 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다

import re
p = re.compile('[a-z]+')
m = p.match('python')
print(m.group())
print(m.start())
print(m.end())
print(m.span())
# match 메서드는 항상 문자열의 시작부터 조사하기 때문에
# match 객체의 start()의 결괏값은 항상 0일 수 밖에 없다.

m2 = p.search('3 python')
print(m2.group())
print(m2.start())
print(m2.end())
print(m2.span())
# 만약 search 메서드를 사용했다면 start() 값은 다르게 나온다.

# 모듈 단위로 수행하기
p2 = re.compile('[a-z]+')
m3 = p2.match('python')
# 위 코드는
m4 = re.match('[a-z]+', 'python')
# 과 같이 축약할 수 있다.
# 한 번 만든 객체를 여러 번 사용해야 할 때는 이 방법보다 re.compile을 사용하자
