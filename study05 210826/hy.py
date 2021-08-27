# lambda와 filter를 이용하여
# ['paper', 'sunflower', 'ketchup', 'mustard', 'pen', 'hamburger', 'spoon', 'couch']
# 리스트에서 a가 들어간 단어만 찾아보세요
li = ['paper', 'sunflower', 'ketchup', 'mustard', 'pen', 'hamburger', 'spoon', 'couch']
li2 = filter(lambda x: 'a' in x, li)
li3 = list(li2)
print(li3)
# 한줄로 바꾸면:
print(list(filter(lambda x: 'a' in x, ['paper', 'sunflower', 'ketchup', 'mustard', 'pen', 'hamburger', 'spoon', 'couch'])))





# 시험 성적표를 받은 당신, 한 과목이라도 50점 미만이면 회초리가 기다리고 있다
# lambda와 map으로 성적을 위조하여 부모님에게 칭찬을 받아 보자
# (당신의 과목당 점수는 random 모듈을 사용하여 생성하자)
# 예시: random신이 점지해주신 당신의 점수 [1, 62, 9, 31, 67, 93]
# 조작 후 점수: [51, 62, 59, 81, 67, 93]
import random as r
grades = []
while len(grades) < 6:
    grades.append(r.randint(0, 100))
print(grades)
new = map(lambda x: x if x > 50 else x + 50, grades)
print(list(new))
