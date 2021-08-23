# 11651 - 좌표 정렬하기 2
## 문제
```
2차원 평면 위의 점 N개가 주어진다. 
좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력:
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 
좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

출력: 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
```

## 풀이
기존 좌표 정렬문제와 반대로 y좌표가 증가하는 순으로 오름차순 정렬하고   
이후 y좌표가 같으면 x좌표가 증가하는 순서로 오름차순 정렬하는 문제.

기본 sort함수에 조건을 걸어주는 방식으로 정렬하는데, **sort 함수 내부에 다중조건**을 주어 정렬한다.

```python
sort_y = sorted(xylist,key = lambda x : (x[1],x[0]))
```
```sort``` 또는 ```sorted``` 함수 내부에 ```lamda x : (x[1],x[0])```를 사용.   
뒤 요소(y)를 우선 정렬하고, 이후 x요소를 정렬하도록 규칙을 설정하였다.

```python
for i in range(n):
    print(sort_y[i][0], sort_y[i][1])
```
이후 정렬된 요소를 n만큼 반복하여 출력한다.


# 소스코드
## PyPy3(시간초과 방지)
```python
# 1
n = int(input())
xylist = []

for i in range(n):
    [x, y] = map(int,input().split())
    xylist.append([x, y])

sort_y = sorted(xylist,key = lambda x : (x[1],x[0]))

for i in range(n):
    print(sort_y[i][0], sort_y[i][1])
```
## python 소스코드(import sys)
```python
# 2
import sys
input = sys.stdin.readline

n = int(input())
xylist = []

for i in range(n):
    [x, y] = map(int,input().split())
    xylist.append([x, y])

sort_y = sorted(xylist,key=lambda x : (x[1],x[0]))

for i in range(n):
    print(sort_y[i][0], sort_y[i][1])
```