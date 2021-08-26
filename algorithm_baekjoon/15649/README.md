# 15649 - N과 M(1)

## 문제
```
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
    1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 
중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
```

## 풀이
백트래킹 알고리즘. 깊이 우선 탐색을 기반으로 한 알고리즘이 사용된 문제.   
```N개의 자연수 중에서 중복 없이 M개를 고른 수열```은 **순열**에 해당한다.
파이썬 내장 함수의 itertools를 import하여 풀수도 있다.

### **#1**
```py
visited = [False] * n
numlist = []
```
먼저 해당 값을 탐색했는지의 여부를 확인하기 위한 배열과 출력 배열을 하나 만들어준다.

### **#2**
```py
if depth == m:
        print(' '.join(map(str, numlist)))
        return
```
만약 선택한 경우의 수가 길이(m개)에 해당한다면 리스트에 추가시키고 출력한다.

### **#3**
```py
for i in range(len(visited)):
    if visited[i]:
        continue
    elif not visited[i]:
        visited[i] = True
        numlist.append(i+1)
        dfs(depth+1,n,m)
        visited[i] = False
        numlist.pop()
```
이미 탐색했던 숫자라면 해당 숫자를 제외하고 계속 탐색한다.

만약 탐색하지 않았던 숫자라면 visited배열(탐색 여부)에 체크해주기 위해 True로 바꾸고 배열을 추가해준다.   
그다음 재귀함수를 호출하며 탐색한 i를 기준으로 하나식 제외하며 깊이우선 탐색한다.

이후 방문했던 배열은 초기화해주기 위해 False로 바꾸어 주고 배열에서 제거한다(pop)

# 소스코드
```py
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
visited = [False] * n
numlist = []

def dfs(depth,n,m):
    if depth == m:
        print(' '.join(map(str, numlist))) # 공백 제거
        return

    for i in range(len(visited)):
        if visited[i]:
            continue
        elif not visited[i]:
            visited[i] = True
            numlist.append(i+1)
            dfs(depth+1,n,m)
            visited[i] = False
            numlist.pop()

dfs(0,n,m)
```

### *itertools를 이용하여 풀기
```py
from itertools import permutations
    n,m = map(int,input().split())
    arr = list(range(1,n+1))
    
    k=list(permutations(arr,m))
    
    for i in k:
        print(' '.join(map(str,i)))
```