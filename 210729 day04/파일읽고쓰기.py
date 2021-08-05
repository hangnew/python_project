# f = open("new.txt", 'w')
# f.close()

# f = open("new.txt", 'w')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# f = open("new.txt", 'r')
# line = f.readline()
# print(line)
# f.close()

# f = open("new.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

# f = open("new.txt", 'r')
# lines = f.readlines()
# for line in lines:
#     line = line.strip()
#     print(line)
# f.close()

# f = open("new.txt", 'r')
# data = f.read()
# print(data)
# f.close()

# f = open("new.txt", 'a')
# for i in range(11, 20):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# with open("new.txt", 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         line = line.strip()
#         print(line)
