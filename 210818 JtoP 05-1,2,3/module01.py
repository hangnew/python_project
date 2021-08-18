# 모듈 사용 방법 : import 모듈이름
# 모듈의 모든 함수를 import할 때 : from 모듈이름 import *
import mod1
from mod1 import *

# print(mod1.add(3, 4))
# print(mod1.sub(4, 2))
print(add(3, 4))
print(sub(4, 2))

# mod1 모듈을 import할 경우, mod1.py의 __name__ 변수에는 모듈이름인 mod1이 저장된다.
print(mod1.__name__)
