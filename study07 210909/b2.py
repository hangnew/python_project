# "헬로 World"에서 영어를 *로 변환하고,
# 다음에 한글을 *로 변환하라.

import re

string1 = '헬로 World'
eng = re.sub(r'[a-zA-Z]', '*', string1)
print(eng)

korean = re.sub(r'[^a-zA-Z ]', '*', string1)
print(korean)
