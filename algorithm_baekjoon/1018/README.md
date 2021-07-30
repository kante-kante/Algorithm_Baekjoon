# 백준 1018 - 체스판 다시 칠하기
## 문제
```
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져있는 M*N 크기의 보드를 찾았다.

어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색.
지민이는 이 보드를 잘라서 8*8 크기의 체스판으로 제작하려 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.
체스판을 색칠하는 경우는 두가지 뿐이다. 하나는 맨 왼쪽 위 칸이 흰색이거나, 또는 검은색인 경우.

8*8 크기는 아무데서나 골라도 된다.
다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

입력: 첫째 줄에 N 과 M이 주어진다.
N,M은 8 <= N,M <= 50.
둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다.
B는 검은색, W는 흰색

출력: 첫째 줄에 지민이가 다시 칠해야 하는 정사각형의 최솟값을 출력.
```

### 풀이
### #1
```python
N,M = map(int,input().split()) # n: 행 개수, M: 열 개수
wblist = []

for i in range(N):
    wblist.append(input())
```
N * M 보드에서 N은 행, M은 각 열을 의미한다.   
이후 행렬, 배열의 형태로 나타내기 위해 리스트를 하나 선언해주고, 반복문을 이용하여 원래 체스판 행의 갯수를 미리 지정해준다.(N)
- - - 
### #2
```python
result = []

for i in range(N-7):
    for j in range(M-7):
        white = 0
        black = 0
```
이후 결과 배열을 표시하기 위해 리스트를 다시 하나 선언해준다.   

체스판에서 **첫 시작점인 첫번째 행을 지정**해주기 위하여 다음과 같이 N-7로 인덱스를 고정시킨다.   
첫 시작점을 지정한 다음 첫 칸(열)을 지정하기 위해 M도 인덱스를 고정시켜준다.(m-7)

문제에서 맨 왼쪽 위 칸(첫번째)이 흰색이거나 검은색인 경우에만 색칠한다고 하였으므로   
W로 시작할 경우와 B로 시작할 경우를 구분짓기 위해 white, black을 각각 0으로 초기화 시켜준다.
- - - 
### #3
```python
for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l) % 2 == 0:          # 짝수
                    if wblist[k][l] != 'W':
                        white += 1
                    if wblist[k][l] != 'B':
                        black += 1
                else:                       # 홀수
                    if wblist[k][l] != 'B':
                        white += 1
                    if wblist[k][l] != 'W':
                        black += 1
        result.append(white)
        result.append(black)

print(min(result))
```

그다음 반복문을 이용하여 첫번째 행,열(i,j)부터 8번째까지 모두 확인한다.   
행, 열의 인덱스의 합이 짝수인 경우에는(인덱스 번호가 같은 경우) 시작점과 같은 색상을 가지고   
인덱스의 합이 홀수인 경우에는 시작점과 다른 색상을 가진다.


인덱스의 합이 짝수일 때 흰색 판이 아니라면 흰색을 칠해줘야 하므로 흰색 인덱스에 +1,   
검은색이 아니라면 검은색으로 칠해줘야 하므로 검은색 인덱스에 +1 해준다.   
홀수는 그 반대로 실행해주면 된다.

이후 출력값은 최솟값을 구해주라고 하였으므로 result에 포함된 것들 중 가장 작은 수를 출력한다.   
```
ex)
W B W B
B W B W
->
0,0(짝) 0,1(홀) 0,2(짝) 0,3(홀)
1,0(홀) 1,1(짝) 1,2(홀) 1,3(짝)
-> 짝수끼리는 같은 색, 홀수끼리 같은 색
```

## 소스코드
```python
N,M = map(int,input().split()) # n: 행 개수, M: 열 개수
wblist = []

for i in range(N):
    wblist.append(input())

result = []

for i in range(N-7):
    for j in range(M-7):
        white = 0
        black = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l) % 2 == 0:          # 짝수
                    if wblist[k][l] != 'W':
                        white += 1
                    if wblist[k][l] != 'B':
                        black += 1
                else:                       # 홀수
                    if wblist[k][l] != 'B':
                        white += 1
                    if wblist[k][l] != 'W':
                        black += 1
        result.append(white)
        result.append(black)

print(min(result))
```
