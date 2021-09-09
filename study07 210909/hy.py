# 정규식을 사용해 이메일만 골라내서 하나씩 프린트해보세요
# string = """
# purple smurf667@aol.com, send a message bill@billwaldon.com dishwasher blah
# rem54mdds@sbcglobal.net monkey banana peel tommfs1982@hotmail.com
# kakao switch christina-alvarez@gmail.net nintendo sony playstation
# verdun.singh@stanford.edu university thomas tammy@reallybigknockers.net
# disney netflix wavve donkey alexander@null.net pikachu pokemon
# """

import re
string = """
purple smurf667@aol.com, send a message bill@billwaldon.com dishwasher blah 
rem54mdds@sbcglobal.net monkey banana peel tommfs1982@hotmail.com 
kakao switch christina-alvarez@gmail.net nintendo sony playstation 
verdun.singh@stanford.edu university thomas tammy@reallybigknockers.net 
disney netflix wavve donkey alexander@null.net pikachu pokemon
"""

emails = re.findall(r'[\w.-]+[@][\w.-]+', string)
# r : Raw String 규칙
# [\w.-] : 모든 문자, 숫자, ., - 포함된 문자열
# + 1번 이상 반복
# [@] : @ 문자

print(emails)

for email in emails:
    print(email)
