# 정규 표현식 Regular Expressions
# 복잡한 문자열을 처리할 때 사용하는 기법, 줄여서 정규식이라고도 한다

# 정규식 없이 코딩
# 주민등록번호를 포함하고 있는 텍스트의 모든 주민등록번호의 쥣자리를 * 문자로 변경해 보자.

data = """
park 800905-1049118
kim 700905-1059119
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))

# 정규식 코딩
import re

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

# \d : 숫자와 매치, [0-9]와 동일
# \d{6} : 숫자와 매치 + 6번 반복
# (\d{6}) : 그루핑 = \g<1>
# [-] : - 문자
# \g<1> : 첫번째 그룹
