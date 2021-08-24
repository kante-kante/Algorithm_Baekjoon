# 1181 - 단어 정렬
## 문제
```
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
    1. 길이가 짧은 것부터
    2. 길이가 같으면 사전 순으로

입력: 첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 
둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 
주어지는 문자열의 길이는 50을 넘지 않는다.

출력: 조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.
```

## 풀이
```sort```, ```sorted```의 차이점과 정렬조건을 알아야 한다.
```
sort = 원본 리스트를 정렬
sorted = 원본 리스트에는 영향을 주지 않고 정렬.
```
정렬조건은 ```lambda```를 이용하며
문제에서 제시한 조건인 길이가 짧은 순서부터 먼저 정렬하고   
길이가 같으면 사전 순으로 정렬한다.

```python
import sys
input = sys.stdin.readline
```
python에서의 ```input()```은 느리기 때문에 readline으로 받아주면 좀 더 빠르게 처리할 수 있다.   
해당 코드를 사용하지 않을 경우, 백준 PyPy3에서 디버깅을 시도하면 된다.
- - - 
### #1
```python
for i in range(n):
    textlist.append(input().strip())
```

입력을 받는 과정에서 공백 제거함수 ```strip```를 사용한 이유는   
아래 lambda식을 사용하면 정렬 시, 공백을 포함하여 리스트에 추가된다.      
이때, 공백을 제거해주기 위해 ```strip```을 이용하여 공백을 제거하고 리스트에 추가한다.

### #2
```python
textlist = sorted(list(set(textlist)), key = lambda x : (len(x),x))
```

sort 함수는 문자열도 정렬해주기 때문에 따로 반복문을 이용하여 정렬할 필요는 없다.   
해당 조건에서 길이 순서대로 오름차순 정렬하고, 같으면 사전 순으로 정렬하도록 조건을 추가하였다.

이후 리스트의 갯수만큼 반복하며 한줄씩 출력한다.

# 소스코드
```python
#1 Python 코드
import sys
input = sys.stdin.readline

n = int(input())
textlist = []

for i in range(n):
    textlist.append(input().strip())

textlist = sorted(list(set(textlist)), key = lambda x : (len(x),x))

for i in range(len(textlist)):
    print(textlist[i])
```
```py
#2 PyPy3 코드
n = int(input())
textlist = []

for i in range(n):
    textlist.append(input().strip())

textlist = sorted(list(set(textlist)), key = lambda x : (len(x),x))

for i in range(len(textlist)):
    print(textlist[i])
```
