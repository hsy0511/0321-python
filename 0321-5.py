'''a = open("C:/test/새파일.txt", 'r')
while True:
    b = a.readline()
    if not b: break
    print(b)
a.close()'''

'''a = open("C:/test/파일.txt",'w')
for b in range(1,11):
    c="%d번째 줄을 입력했습니다\n"%b
    a.write(c)
    print(c)
a.close()'''

a = open("C:/test/파일.txt",'r')
while True:
    b=a.readline()
    if not b : break
    print(b)
a.close()

