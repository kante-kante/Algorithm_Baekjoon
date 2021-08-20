# 11650 - 좌표 정렬하기

## 문제
```
2차원 평면 위의 점 N개가 주어진다. 
좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 
좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

출력
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
```

## 풀이

**정렬 및 인덱싱**이 중요한 문제.

```python
for i in range(n):
    [x, y] = map(int,input().split())
    xylist.append([x, y])
```
배열에 두개의 요소를 입력받기 위해서는 map 함수를 이용하여 처리하면 되고   
배열에 삽입할 때에는 ```[x, y]``` 처럼 요소를 구분지어 넣어주면 된다.

```python
xylist.sort()

for i in range(n):
    print(xylist[i][0], xylist[i][1])
```
문제에서 제시한 조건중 하나인 x좌표가 같으면 y좌표가 증가하는 순서로 정렬하면 되는데   
sort함수에서는 값이 같으면 알아서 낮은 요소부터 오름차순 정렬시킨다.


이후 정렬된 요소를 반복문을 통해 출력해주면 된다.   
첫번째 코드는 PyPy3로 제출(시간초과 오류)   
두번째 코드는 python으로 제출 가능하다.

# 소스코드
## #1 PyPy3
```python

n = int(input())
xylist = []

for i in range(n):
    [x, y] = map(int,input().split())
    xylist.append([x, y])

xylist.sort()

for i in range(n):
    print(xylist[i][0], xylist[i][1])
```
## #2 python
```python
#2
import sys
input = sys.stdin.readline

n = int(input())
xylist = []

for i in range(n):
    [x, y] = map(int,input().split())
    xylist.append([x, y])

xylist.sort()

for i in range(n):
    print(xylist[i][0], xylist[i][1])
```

