'''a = input("아무거나 입력하세요 :") # input은 입력되는 모든것을 문자열 처리 하여 숫자가 들어가도 그 숫자는 문자열이다.
print(a)'''

'''a = open("C:/test/새파일.txt", 'w')
print(type(a))
for b in range(1, 11):
    c = "%d번째 줄입니다.\n" % b
    a.write(c)
a.close()
'''
a = open("C:/test/새파일.txt", 'r')
while True:
    b = a.readline()
    if not b: 
        print("if not b",b)
        break

    #print(b)
a.close()