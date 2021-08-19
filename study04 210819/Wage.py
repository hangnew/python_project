class Person:
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn

class Ceo(Person):
    def w(self, wage):
        print(self.name, self.ssn, wage)

Ceo('홍길동', '901112').w('천만원')
