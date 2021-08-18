# 특정 디렉터리의 모듈을 *를 사용하여 import할 때
# 해당 디렉터리의 __init__.py 파일에
# __all__ 변수를 설정하고 import할 수 있는 모듈을 정의해 주어야 한다.

# __all__이 의미하는 것은
# sound 디렉터리에서 *기호를 사용하여 import할 경우
# 이곳에 정의된 echo 모듈만 import된다는 의미이다.
__all__ = ['echo']
