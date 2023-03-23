a = open("C:/test/새파일.txt", 'r')
b = a.readlines()
for c in b:
    print(c)
a.close()