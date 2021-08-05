'''
2447 - 별 찍기 - 10

문제
재귀적인 패턴으로 별을 찍어보자. N이 3의 거듭제곱(3,9,27...)이라고 할 때,
크기 N의 패턴은 N * N 정사각형 모양이다.

크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)*(N/3) 정사각형을 크기 N/3의 패턴으로
둘러싼 형태이다.

입력: 첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다.
즉, 어떤 정수 k에 대해 N=3^k이며, 이때 1<= k <8 이다.
출력: 첫째 줄부터 N번째 줄까지 별을 출력한다.

풀이
위 문제는 프랙탈 구조의 도형을 그리는 문제.
해당 문제는 재귀와 분할 정복 알고리즘이 사용된다.

```
***
* *
***
```
다음과 같이 이루어진 구조가 반복되는 모습을 보인다.

입력값이 9인 경우를 살펴보면
```
  0 1 2 3 4 5 6 7 8
0 * * * * * * * * *
1 *   * *   * *   *
2 * * * * * * * * *
3 * * *       * * *
4 *   *       *   *
5 * * *       * * *
6 * * * * * * * * *
7 *   * *   * *   *
8 * * * * * * * * *
```

다음과 같은 형태로 나오게 된다. 
지수가 i일 때, 별을 찍으면 3^i일 때에는 3^(i-1)의 별 배열이 찍힌다.

square -> (입력받은 n의 지수) - 1이 되며
```python
for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
```
해당 부분은 가운데에 공백을 생성 및 별을 그려주는 코드가 된다.


아래 코드는 2차원 배열을 이용하여 저장한 방식이며
3^1일때의 별 데이터를 먼저 그리는데 두번째줄만 공백을 생성해준다.
(0=공백, 1=별)
'''
def star(n):
    matrix = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return matrix

pattern = ["***","* *","***"]
n = int(input())
square = 0

while n != 3:
    n = int(n / 3)
    square += 1

for i in range(square):
    pattern = star(pattern)

for i in pattern:
    print(i)

# 다른 소스코드
# 별 찍는 재귀 함수
def draw_star(n) :
    global Map
    
    if n == 3 :
        Map[0][:3] = Map[2][:3] = [1]*3
        Map[1][:3] = [1, 0, 1]
        return

    a = n//3
    draw_star(n//3)
    for i in range(3) :
        for j in range(3) :
            if i == 1 and j == 1 :
                continue
            for k in range(a) :
                Map[a*i+k][a*j:a*(j+1)] = Map[k][:a] # 핵심 아이디어

N = int(input())      

# 메인 데이터 선언
Map = [[0 for i in range(N)] for i in range(N)]

draw_star(N)

for i in Map :
    for j in i :
        if j :
            print('*', end = '')
        else :
            print(' ', end = '')
    print()