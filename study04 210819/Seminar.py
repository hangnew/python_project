seminarA = set(['홍길동', '김길동', '박길동', '정길동'])
seminarB = set(['홍길동', '박길동', '황길동'])

# names = []
# for i in seminarA:
#     for j in seminarB:
#         if i == j:
#             names.append(i)

print(seminarA & seminarB)
print(seminarA.intersection(seminarB))
