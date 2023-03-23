a = open("C:/test/새파일.txt", 'a')
for b in range(11,20) :
    c = "%d번째 줄입니다.\n" % b
    a.write(c)
a.close