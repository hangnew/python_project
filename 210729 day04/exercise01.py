# a110 : a는 부서를 나타냄, 1: 직급, 10:내 번호
# 부서가 a:기획부, b:개발부, c:인사부
# 직급이 1:사장, 2:팀장, 3:사원
# 처리
# 1.입력한 데이터 중에서 부서와 직급을 추출한다.
# 2.부서의 값에 따라서 부서를 판별
# 3.직급의 값에 따라서 직급을 판별
# a110, b230, c340

while True:
    code = input('당신의 사원 번호를 입력하세요 (종료:x) >> ')
    if code == 'x':
        print('시스템을 종료합니다.')
        break
    depart = code[0]
    level = code[1]
    result = ''
    if depart == 'a':
        result = '기획부'
    elif depart == 'b':
        result = '개발부'
    elif depart == 'c':
        result = '인사부'
    else:
        result = '존재하지 않는 부서입니다.'
    if level == '1':
        result = result + ' 사장'
    elif level == '2':
        result = result + ' 팀장'
    elif level == '3':
        result = result + ' 사원'
    else:
        result = result + '존재하지 않는 직급입니다.'
    print('당신은 ' + result)
