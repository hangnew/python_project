# relative 패키지
# .. 부모 디렉터리
# . 현재 디렉터리

from ..sound.echo import echo_test

def render_test():
    print("render")
    echo_test()

render_test()
