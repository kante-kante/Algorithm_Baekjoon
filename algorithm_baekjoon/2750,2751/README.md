# 2750 - 수 정렬하기

## 문제
```
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오

입력: 첫째 줄에 수의 개수 N(1<=N<=1000)이 주어진다. 둘째 줄부터 N개의 줄에는
수가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력: 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
```

## 풀이
```python
n = int(input())
nlist = []

for i in range(n):
    nlist.append(int(input()))
```
첫번째에는 수의 갯수를 입력받고 수의 갯수만큼 다시 수를 입력받아야 한다.   
n은 수의 개수를, 첫번째 반복문에서는 n개만큼 수를 입력받고 이를 리스트에 삽입한다.

```python
nlist.sort()
```
삽입한 다음 수를 오름차순 정렬해야하므로 sort() 함수를 이용하여 수를 정렬한다.

```python
for i in range(len(nlist)):
    print(nlist[i])
```
그리고 리스트의 갯수만큼 반복하며 리스트 내부의 값을 출력한다.

## 2751번
위의 풀이 방법과 동일하지만, 백준 채점 인터프리터를 pypy로 설정하지 않으면 시간초과 발생.

# 소스코드
```py
n = int(input())
nlist = []

for i in range(n):
    nlist.append(int(input()))

nlist.sort()
for i in range(len(nlist)):
    print(nlist[i])
```