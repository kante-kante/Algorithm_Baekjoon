'''
10814 - 나이순 정렬
문제
온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 
이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

입력:
첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)
둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 
나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 
이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다. 
입력은 가입한 순서로 주어진다.

출력:
첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 
한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.

풀이
문제에서 제시한 조건을 잘 확인하지 않으면 디버깅 오류를 범할수 있다.
```
조건
1. 나이는 1 <= N <= 200인 정수
2. 이름은 알파벳 대소문자. 길이 <= 100인 문자열
```
### #1
```py
import sys
input = sys.stdin.readline

n = int(input())
userlist = []
```
먼저 입력받은 숫자만큼 나이와 이름을 추가해야 하므로 반복문을 사용하여 추가한다.
파이썬의 input()은 느리기 때문에 readline을 사용하여 입력받으면 빠르게 처리할 수 있다.

```py
for i in range(n):
    [age, name] = input().split()
    userlist.append([int(age),str(name)])
```
나이와 이름으로 이루어진 배열 요소를 공백 ```split()```을 이용하여 입력받고
userlist에 요소를 삽입할 때에는 각각 형변환을 해주어 삽입해주면 된다.
(문제에서 나이는 정수, 이름은 문자열이라고 하였으므로)

```py
userlist.sort(key = lambda x: x[0])
```
이후 정렬조건에 ```lambda```를 이용하여 추가해준다.
회원들을 나이가 증가하는 순으로, 
나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하라고 하였으므로
key 조건에 첫번째 요소인 나이만을 기준으로 정렬하면 뒤에 붙은 이름순 정렬을 제외할 수 있다.

이후 userlist에 있는 요소의 길이만큼 반복하여 한줄씩 출력한다.
'''
import sys
input = sys.stdin.readline

n = int(input())
userlist = []

for i in range(n):
    [age, name] = input().split()
    userlist.append([int(age),str(name)])

userlist.sort(key = lambda x: x[0])

for i in range(len(userlist)):
    print(userlist[i][0],userlist[i][1])