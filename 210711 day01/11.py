# id = input('로그인할 id를 입력>> ')
# if id == 'root':
#     print('로그인되었습니다.')
# else:
#     print('로그인 실패')

sticker_Price = 1000
sticker_Count = 3
bookmark_Price = 2500
bookmark_Count = 4
sum = sticker_Price * sticker_Count + bookmark_Price * bookmark_Count
total_Amount = int(sum - sum * 0.1)
print(total_Amount)