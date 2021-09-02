#간단한 타자연습 프로그램 만들기
#진행할 짧은 글 연습 개수를 입력받아, 해당하는 만큼의 연습을 진행하고
#정확도(소수점 없는 백분율)와 걸린시간(초)를 출력하는 프로그램(함수) typing_game을 만들어보세요
#연습 개수의 경우 사용자가 정수만 입력한다고 가정합니다
#연습 문장은 제시된 리스트에서 랜덤으로 나오도록 해주세요

import time
import random
sentences = ['String sql = "select * from member";',
             '@Controller',
             '@Autowired',
             '@RequestMapping()',
             '@Repository',
             'static SingleObject object;',
             'public static SingleObject getInstance()',
             'Connection con = DriverManager.getConnection(url, user, password);',
             'Class.forName("com.mysql.jdbc.Driver");',
             'PreparedStatement ps = con.prepareStatement(sql);']

def typing_game(n):
    i = 0
    total_sum = 0
    correct_sum = 0
    while i < int(n):
        sentence = random.choice(sentences)
        total_sum += len(sentence)
        correct = 0
        print(sentence)
        sentence2 = input()
        for j in range(len(sentence)):
            if sentence[j] == sentence2[j]:
               correct += 1
        correct_sum += correct
        i += 1
    print(correct_sum / total_sum * 100)

#실행문장
print("타자 연습에 오신 것을 환영합니다")
n = input("몇 줄의 짧은 글 연습을 하시겠어요?(1 이상의 정수) >> ")
typing_game(n)
