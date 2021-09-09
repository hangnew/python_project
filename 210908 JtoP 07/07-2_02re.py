# re : regular expression 파이썬 정규 표현식 지원 모듈
import re

# p = re.compile('ab*')
# re.compile을 사용하여 정규 표현식을 컴파일하여 컴파일된 패턴 객체를 p에 담아준다.
# 패턴이란 정규식을 컴파일한 결과이다.

# 컴파일된 패턴 객체를 사용하여 문자열 검색을 수행해 보자.
# match() : 문자열의 처음부터 정규식과 매치되는지 조사한다. (반환 : match 객체 || None)
# search() : 문자열 전체를 검색하여 정규식과 매치되는지 조사한다. (반환 : match 객체 || None)
# findall() : 정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다.
# finditer() : 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려준다.





# 1. match()
# 문자열의 처음부터 정규식과 매치되는지 조사한다. (반환 : match 객체 || None)
p = re.compile('[a-z]+')
# m = p.match('python')
# print(m)
# 'python' 문자열은 [a-z]+ 정규식에 부합되므로 match 객체를 돌려준다.

# m2 = p.match('3 python')
# print(m2)
# '3 python' 문자열은 처음에 나오는 문자 3이 정규식 [a-z]+ 에 부합하지 않으므로 None을 돌려준다.

# 보통 다음과 같은 흐름으로 작성한다.
# p = re.compile(정규표현식)
# m = p.match('string goes here')
# if m:
#   print('Match found: ', m.group())
# else:
#   print('No match')





# 2. search()
# 문자열 전체를 검색하여 정규식과 매치되는지 조사한다. (반환 : match 객체 || None)
# m = p.search('python')
# print(m)
# 'python' 문자열에 search 메서드를 수행하면 match 메서드를 수행했을 때와 동일하게 매치된다.

# m2 = p.search('3 python')
# print(m2)
# '3 python'의 문자열의 첫 번째 문자는 '3'이지만,
# search는 문자열의 처음부터 검색하는 것이 아니라 문자열 전체를 검색하기 때문에
# '3' 이후의 'python' 문자열과 매치된다.





# 3. findall()
# 정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다.
# result = p.findall('life is too short')
# print(result)
# 'life is too short' 문자열의 'life', 'is', 'too', 'short' 단어를 각각 [a-z]+ 정규식과 매치해서 리스트로 돌려준다.





# 4. finditer()
# 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려준다.
result = p.finditer('life is too short')
print(result)
for r in result: print(r)
# finditer는 findall과 동일하지만 그 결과로 반복 가능한 객체 (iterator object)를 돌려준다
# 반복 가능한 객체가 포함하는 각각의 요소는 match 객체이다
