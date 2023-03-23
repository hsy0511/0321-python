a = open("C:/test/새파일.txt", 'w')
for b in range(1, 11):
    c = "%d번째 줄입니다.\n" % b
    a.write(c)
a.close()