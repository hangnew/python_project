# a = 'select name from member where id = python'
# 1. 첫 단어를 검색하여 crud중 어떤기능을 하는 sql문인지 출력한다.
#
# 2. sql문 a에서 name에 해당하는 부분을 target
#            member에 해당하는 부분을 table
#            python에 해당하는 부분을 id로 그루핑하고
#   a가 어떤 기능을 하는 sql문인지 자세히 출력한다.

import re
a = 'select name from member where id = python'

p = re.compile(r'(?P<crud>\w+)[\s](?P<target>\w+)[\s](\w+)[\s](?P<table>\w+)([\s](\w+)){2}[\s].[\s](?P<id>\w+)')
m = p.search(a)
print(m.group("crud"))
print(m.group("target"))
print(m.group("table"))
print(m.group("id"))
