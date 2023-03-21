# 0321-python
# 사용자의 입력과 출력
## 사용자 입력 (input 사용)
```python
a = input("아무거나 입력하세요 :")
print(a)
```
### 결과값
![image](https://user-images.githubusercontent.com/104752580/226493017-90f2960d-6546-41fc-98b2-f2005511ee3c.png)

변수a를 input을 사용하여 아무거나 입력하세요라는 문구를 출력 후 프롬프트 창에서 아무 문자나 입력하면 변수 a가 print를 통해서 출력 된다.
###### ※ input은 입력되는 모든 것을 문자열로 취급하기 때문에 숫자를 입력해도 숫자가 아닌 문자열인것을 주의하자.
## 사용자 출력 (print 사용)
```python
a = 123
b = "space bar"
c = [1,2,3]
print(a)
print(b)
print(c)
```
### 결과값
![image](https://user-images.githubusercontent.com/104752580/226493921-9a406657-03b5-4321-bd58-4ebc3b85888d.png)

변수 a,b,c의 값을 print로 출력한다.
## print 기타 사용법
```python
print("music" "is" "my" "life")

print("music","is","my","life")

for a in range(10):
    print(a, end=" ")
```
### 결과값
![image](https://user-images.githubusercontent.com/104752580/226494258-5588a82c-4973-40ee-8992-6214ecfa9cc4.png)

큰 따옴표("")로 둘러싸인 문자열은 + 연산과 같다.

문자열에서 콤마는(,) 띄어쓰기를 뜻한다.

end=" "는 한줄 출력을 하는 방법이다.

# 파일 읽고 쓰기
## 파일 생성하기
```python
a = open("새파일.txt", 'w')
a.close()
```
### 파일열기 모드
![image](https://user-images.githubusercontent.com/104752580/226497360-ee277cc4-7d4b-490a-9a12-aaea8e3e95cc.png)

open 함수로 파일을 쓰기모드(w)로 열고, close 함수로 파일을 닫는다. 

파이썬에서 파일경로를 표시할 때는 슬래시(/)로 사용한다.

역슬래시(\)를 사용하려면 \\와 같이 두개를 사용하거나 문자열앞에 r을 붙여 사용해야한다.

###### ※ \n과 같이 이스케이프 문자가 있을 경우 의도했던 파일 경로와 달라지기 때문이다.

###### ※ 파일을 지정 디렉터리에 생성하려면 (C:/디렉터리/파일.txt)로 쓴다.
## 파일을 쓰기 모드로 열어 내용 쓰기 (w:쓰기모드)
```python
a = open("C:/test/새파일.txt", 'w')
for b in range(1, 11):
    c = "%d번째 줄입니다.\n" % b
    a.write(c)
a.close()
```
### 결과값
![image](https://user-images.githubusercontent.com/104752580/226498395-e6f4f2b8-913f-4453-aabe-ab7366ff8a6f.png)


![image](https://user-images.githubusercontent.com/104752580/226498445-81f8cf01-2576-4b06-94a6-5f31db5d2fd9.png)

c드라이브 test디렉터리에 새파일.txt라는 쓰기모드(w) 파일을 열고, write 함수를 통해 값을 적는다. 
## 파일을 읽는 여러 가지 방법 (r:읽기모드)
### readline 함수 이용하기
```python
a = open("C:/test/새파일.txt", 'r')
while True:
    b = a.readline()
    if not b: break
    print(b)
a.close()
```
### 결과값
![image](https://user-images.githubusercontent.com/104752580/226501725-1d77c25d-036a-4cf2-bf91-c6b20ca98b6a.png)

c드라이브 test디렉터리에 새파일.txt라는 읽기모드(r) 파일을 열고, readline 함수를 통해 한줄씩 읽어드린다.

이때 while문을 써서 읽을 줄이 없을때까지 반복하여 읽고, 줄이 없으면 break문으로 while문을 벗어난다. 
### readlines 함수 사용하기
```python
a = open("C:/test/새파일.txt", 'r')
b = a.readlines()
for c in b:
    print(c)
a.close()
```
### 결과값
![image](https://user-images.githubusercontent.com/104752580/226502399-2e2ec5bf-5c20-47c7-947a-43e970aaf772.png)

c드라이브 test디렉터리에 새파일.txt라는 읽기모드(r) 파일을 열고, readlines 함수를 통해 모든줄을 읽어서 각각 줄의 요소로 갖는 리스트를 리턴한다.
###### ※ readline과 readlines를 사용할 때 줄바꿈(\n)을 제거하려면 변수.strip()하는 strip함수를 사용해 제거할 수 있다.
### read 함수 사용하기
```python
a = open("C:/test/새파일.txt", 'r')
b = a.read()
print(b)
a.close()
```
### 결과값
![image](https://user-images.githubusercontent.com/104752580/226502937-fb4b119c-efe5-4c08-8dbe-3f2498cf5d14.png)

c드라이브 test디렉터리에 새파일.txt라는 읽기모드(r) 파일을 열고, read 함수를 통해 파일 전체 내용을 읽어드린다.
### for문 사용하기
```python
a = open("C:/test/새파일.txt", 'r')
for b in a:
    print(b)
a.close()
```
### 결과값
![image](https://user-images.githubusercontent.com/104752580/226503357-9794d793-9071-4176-bb46-0a7a8365aa00.png)

c드라이브 test디렉터리에 새파일.txt라는 읽기모드(r) 파일을 열고, for문을 사용하여 줄단위로 읽어드린다.
## 파일에 새로운 내용 추가하기 (a:추가 모드)
```python
a = open("C:/test/새파일.txt", 'a')
for b in range(11,20) :
    c = "%d번째 줄입니다.\n" % b
    a.write(c)
a.close
```
### 결과값
![image](https://user-images.githubusercontent.com/104752580/226515233-c3843ab4-43d2-418a-a5b4-ceafeefdc7aa.png)

c드라이브 test디렉터리에 새파일.txt라는 추가모드(a) 파일을 열고, write를 통해 기존에 있던 내용 다음부터 값을 적기 시작한다.

## with문 사용하기
```python
with open("C:/test/새파일2.txt", "w") as a:
    a.write("hello, world")
```
### 결과값
![image](https://user-images.githubusercontent.com/104752580/226522016-046720e5-ec6a-40ad-9cd3-185615268664.png)
![image](https://user-images.githubusercontent.com/104752580/226522041-3582f197-5537-4d25-bd7e-ddb7be3d7b97.png)

with는 open과 close를 자동으로 처리할 수 있는 역할로 만들어졌다.
