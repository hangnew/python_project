# try ~ except : 오류 종류와 상관 없이 except 수행
# try ~ except 발생 오류 : 미리 정해 놓은 오류 이름과 일치할 때만 except 수행
# try ~ except 발생 오류 as 오류 메시지 변수 : 오류 메시지의 내용까지 알고 싶을 때 사용한다

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

# try ~ finally : try문 수행 도중 예외 발생 여부 상관없이 항상 수행
# 보통 finally절은 사용한 리소스를 close해야 할 때 많이 사용한다.

# try ~ except ~ else : 오류가 없을 경우 else절이 수행된다.
try:
    age = int(input('나이를 입력하세요'))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다')

# try ~ except pass : 특정 오류가 발생할 경우 그냥 통과시키고자 할 때
try:
    f = open("없는 파일", 'r')
except FileNotFoundError:
    pass
