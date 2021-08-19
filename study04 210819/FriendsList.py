l1 = []
def add(name):
    l1.append(name)

def delete(name):
    l1.remove(name)

while True:
    print('1. 친구 리스트 출력')
    print('2. 친구 추가')
    print('3. 친구 삭제')
    print('4. 이름 변경')
    print('9. 종료')
    i = input('메뉴를 선택하세요>> ')
    if i == '9':
        break
    elif i == '1':
        print(l1)
    elif i == '2':
        n = input('추가할 친구 입력>> ')
        add(n)
    elif i == '3':
        n = input('삭제할 친구 입력>> ')
        delete(n)
    elif i == '4':
        n = input('변경할 친구 입력>>')
        n2 = input('변경될 이름 입력>> ')
        delete(n)
        add(n2)
    else:
        print('다시 선택하세요')
