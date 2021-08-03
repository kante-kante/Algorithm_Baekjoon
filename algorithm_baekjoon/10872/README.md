# 백준 10872 - 팩토리얼

## 문제
```
0보다 크거나 같은 정수 N이 주어진다. 이때 N!을 출력하는 프로그램을 작성하시오.

입력: 첫째 줄에 정수 N(0<=N<=12)가 주어진다.
출력: 첫째 줄에 N!을 출력한다.
```

## 풀이   
단순 반복문을 사용하여 출력할수도 있겠지만 그렇게 하면 재귀함수를 사용하는 방식이 아니므로 제외.

```python
else:
    return N * factorial(N-1)
```
재귀는 같은 함수가 계속 반복되는 형태이므로, 아래 코드에서 사용한 재귀는
else에 있는 return값이 재귀함수를 호출하는 부분이 된다.
<br/><br/>

```python
def factorial(N):
    if N == 0 or N == 1:
        return 1
```
첫번째 조건문에서 N이 0이거나 1인 경우에는 1값으로 리턴하도록 설정.(0!은 1로 약속. 음수 팩토리얼은 계산 불가.)   
else문에서는 0또는 1이 아닌 경우에는 10 * 9 * 8....등으로 계산되도록 재귀함수 호출.
- - -

```python
from math import factorial
print(factorial(int(input())))
```
더 쉬운 방법을 사용하려면 파이썬에서 제공하는 factorial 함수를 불러오면 된다.


## 소스코드
```python
N = int(input())

def factorial(N):
    if N == 0 or N == 1:
        return 1
    else:
        return N * factorial(N-1)

print(factorial(N))
```
## 소스코드(함수 호출)
```python
from math import factorial
print(factorial(int(input())))
```