# 아이디 유효성 검사
# 영문과 숫자만으로 아이디를 입력하는데 5자 미만이거나 16자 초과인 경우 "유효하지 않은 아이디입니다." 출력
# 5자 이상 15자 이하인 경우 유효한 아이디입니다." 출력

import re

def check(id):
    p = re.compile(r'[\w]{5,16}$')
    m = p.match(id)
    if m:
        print('유효한 아이디입니다')
    else:
        print('유효하지 않은 아이디입니다')

# 5자 미만
id1 = 'abc'
# 16자 초과
id2 = 'abcdefgh1234599678aaa'
# 특수문자
id3 = 'wow!@@!!'
# 유효
id4 = 'abcde123'

check(id1)
check(id2)
check(id3)
check(id4)
