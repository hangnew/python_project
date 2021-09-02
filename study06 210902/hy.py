# 1. 사용자의 입력값 중 숫자만 골라내 그래프를 그려주는 프로그램을 만드세요.
# 예시) 입력>> dig6aa2346dc103bbb05
# 출력)
# *       *
# *       *         *
# *     * *         *
# *   * * *     *   *
# * * * * *     *   *
# * * * * * *   *   *
# 6 2 3 4 6 1 0 3 0 5

# 입력받은 문자열 중 숫자만 filter해준다
numbers = list(filter(lambda x: x.isdecimal(), input('입력>> ')))
# 그래프의 가로길이 = 숫자 개수
width = len(numbers)
# 그래프의 세로길이 = 가장 높은 숫자
height = int(max(numbers))
# 세로 길이를 변수 하나에 일단 저장
row = height

# 그래프의 세로 길이만큼 별표찍기가 반복됨, i = 행
for i in range(height):
    # 가로길이만큼 별을 찍는다. j = 열
    for j in range(width):
        # 입력받은 문자열 중 row보다 같거나 크다면 * 찍기, 아니면 공백
        if int(numbers[j]) >= row:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    # row = row - 1
    row -= 1
    print()

# for문으로 입력받은 숫자 출력, end=' ' 한 줄로 출력 후 print()로 줄바꿈
for number in numbers:
    print(number, end=' ')

# 2. sys모듈을 사용해 cmd에서 아래의 명령어로 실행되는 프로그램을 만드세요
# sys 출력 함수 : sys.stdout.write()
# 예시) python graph.py abcd8u30103sdji209u731ls1948
# 출력)
#                 *         *
# *               *         *   *
# *               * *       *   *
# *               * *       *   *
# *               * *       *   *
# *               * *       * * *
# * *       *     * * *     * * *
# * *       * *   * * *     * * *
# * *   *   * *   * * * * * * * *
# 8 3 0 1 0 3 2 0 9 7 3 1 1 9 4 8
