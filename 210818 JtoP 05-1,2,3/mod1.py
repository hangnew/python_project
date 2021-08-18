# mod1.py
# 파이썬 확장자 .py 파일은 모두 모듈이다.

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# mod1.py 파일을 실행할 경우 mod1.py의 __name__ 변수에는 __main__ 값이 저장된다.
print(__name__)

# print(add(1, 4))
# print(sub(4, 2))

# 직접 mod1.py를 실행하면 __name__ == "__main__" 이 참이 되어 if문 다음 문장이 수행되지만,
# 다른 곳에서 mod1 모듈을 불러서 사용할 때는 거짓이 되어 if문 다음 문장이 수행되지 않는다.
if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))
