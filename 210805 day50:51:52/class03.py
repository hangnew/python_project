# 클래스 변수

class Family:
    lastname = '김'

print(Family.lastname)

# 클래스 변수는 클래스로 만든 모든 객체에 공유된다.
Family.lastname = '박'
print(Family.lastname)

