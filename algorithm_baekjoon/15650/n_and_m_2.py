'''
15650 - N과 M(2)
문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
- 고른 수열은 오름차순이어야 한다.

입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 
중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

풀이
기존 15649 - n과 m 순열 문제와 비슷하지만 값을 오름차순으로 정렬해야한다는 것이 다른 문제.
해당 문제에서는 [1,2],[2,1] 을 중복되는 경우로 보기 때문에 해당 중복값을 제외하고 출력해야 한다.

```py
for i in range(index,n):
        if not visited[i]:
            visited[i] = True
            numlist.append(i+1)
            dfs(depth+1,i+1,n,m)
            visited[i] = False
            numlist.pop()
```
중복되는 값을 피하기 위해서 이전의 인덱스 값을 저장하는 index 변수를 추가하여
index + 1 값부터 진행하도록 하는 방법.

```py
for i in range(depth,n):
    if not visited[i]:
        visited[i] = True
        numlist.append(i+1)
        dfs(depth+1,n,m)
        numlist.pop()

        for j in range(i+1,n):
            visited[j] = False
```
이미 방문했던 visited 배열을 제외하고(i+1) 중복되지 않도록 for문을 이용하여
visited[]를 False로 바꿔주는 방법이 있다.
'''
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
visited = [False] * n
numlist = []

def dfs(depth,index,n,m):
    if depth == m:
        print(' '.join(map(str, numlist))) # 공백 제거
        return

    for i in range(index,n):
        if not visited[i]:
            visited[i] = True
            numlist.append(i+1)
            dfs(depth+1,i+1,n,m)
            visited[i] = False
            numlist.pop()

dfs(0,0,n,m)


# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# visited = [False] * n
# numlist = []

# def dfs(depth,n,m):
#     if depth == m:
#         print(' '.join(map(str, numlist))) # 공백 제거
#         return

#     for i in range(depth,n):
#         if not visited[i]:
#             visited[i] = True
#             numlist.append(i+1)
#             dfs(depth+1,n,m)
#             numlist.pop()

#             for j in range(i+1,n):
#                 visited[j] = False

# dfs(0,n,m)