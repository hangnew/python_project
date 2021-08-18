# 패키지 안의 함수 실행하기

# echo 모듈을 import하여 실행하는 방법
import game.sound.echo
game.sound.echo.echo_test()

# echo 모듈이 있는 디렉터리까지를 from ... import하여 실행하는 방법
# from game.sound import echo
# echo.echo_test()

# echo 모듈의 echo_test 함수를 직접 import하여 실행하는 방법
# from game.sound.echo import echo_test
# echo_test()

# import game을 수행하면 game 디렉터리의 __init__.py에 정의한 것만 참조할 수 있다.
# import game
# game.sound.echo.echo_test()

# import할 때 가장 마지막 항목은 반드시 모듈 또는 패키지여야 한다.
# import game.sound.echo.echo_test
