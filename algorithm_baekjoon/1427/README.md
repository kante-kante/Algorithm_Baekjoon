# 1427 - 소트 인사이드
## 문제
```
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

입력: 첫째 줄에 정렬하고자하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

출력: 첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.
```

## 풀이
```python
# 1
for i in str(n):
    nlist.append(int(i))

# 반복문 대신 사용
nlist = list(map(int,str(n)) # map함수로 문자열 하나씩을 자르기 때문에 반복문 대신 사용 가능
```

첫 반복문에서 범위를 문자형으로 입력받아야 한다.(int형으로 받으면 object is no iterable)

또는 map 함수를 이용하여 반복문 대신 리스트로 넣어주어도 된다.

```python
# 2
nlist.sort(reverse=True)

for i in nlist:
    print(i,end='')
```
일반적으로 오름차순 정렬 시 sort()를 그냥 사용하면 되지만 문제에서는 내림차순으로 정렬하라고 하였으므로
```reverse = True```로 설정하여 오름차순 정렬을 내림차순으로 바꿔준다.

이후 배열에 저장된 요소들을 하나씩 출력한다.

# 소스코드
```python
n = int(input())
nlist = []

for i in str(n):
    nlist.append(int(i))

# nlist = list(map(int,str(n)) # map함수로 문자열 하나씩을 자르기 때문에 반복문 대신 사용 가능

nlist.sort(reverse=True)

for i in nlist:
    print(i,end='')

```


## 지능형 리스트를 이용한 소스코드
```python
n = input()
nlist = [int(i) for i in n]

nlist.sort(reverse=True)

for i in nlist:
    print(i, end='')
```