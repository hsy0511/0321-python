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
print("music" "is" "mylife")

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
print("hello")
a.close()
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/226497252-b812d278-a559-4818-b3ee-81dd8345767f.png)

open 함수로 파일을 열고, close 함수로 파일을 닫는다. 

파이썬에서 파일경로를 표시할 때는 슬래시(/)로 사용한다.

역슬래시(\)를 사용하려면 \\와 같이 두개를 사용하거나 문자열앞에 r을 붙여 사용해야한다.(\n과 같이 이스케이프 문자가 있을 경우 의도했던 파일 경로와 달라지기 때문이다.

###### ※ 파일을 지정 디렉터리에 생성하려면 (C:/디렉터리/파일.txt)로 쓴다.
### 파일열기 모드
![image](https://user-images.githubusercontent.com/104752580/226497360-ee277cc4-7d4b-490a-9a12-aaea8e3e95cc.png)
