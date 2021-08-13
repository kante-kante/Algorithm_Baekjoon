'''
2108 - 통계학
문제
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는
기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정한다.
1. 산술평균: N개의 수들의 합을 N으로 나눈 값
2. 중앙값: N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
3. 최빈값: N개의 수들 중 가장 많이 나타나는 값
4. 범위: N개의 수들 중 최댓값과 최솟값의 사이
N개의 수가 주어졌을 때, 네가지 기본 통계값을 구하는 프로그램을 작성하시오.

입력: 첫째 줄에 수의 개수 N(1<=N<=500,000)이 주어진다. 단, N은 홀수이다.
그다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

출력:
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
둘째 줄에는 중앙값을 출력한다.
셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
넷째 줄에는 범위를 출력한다.

풀이
처음 statistics 모듈을 import하여 실행했는데 산술평균과 중앙값은 도출되었으나
최빈값에서 원하는 값을 도출할 수 없었고 범위를 구할 수 없었다.
또한, input()을 사용하면 시간 초과가 발생하기 때문에 sys 모듈을 사용하였다.

산술평균은 소수점 첫째자리에서 반올림해야 하므로 round 모듈을 사용하였고
중앙값은 증가하는 순서로 나열되어야 하므로 sort()를 이용하여 정렬하였다.

최빈값을 구하는 과정에서 Counter함수를 이용하였으며
문제에서 제시한 최빈값 중 두번째로 작은 값을 구하여야 하므로
가장 앞에 있는 최빈값의 빈도수와 그 뒤의 빈도수가 같다면 최빈값이 최소 2개 이상 있다는 뜻이므로
두번째 값을 출력해주기 위해 [1][0]으로 출력한다.

범위의 경우 정렬된 맨 마지막 요소 - 첫번째 요소 or max - min으로 구하면 된다.
'''
import sys
from collections import Counter

n = int(sys.stdin.readline())
nlist = []

for _ in range(n):
    nlist.append(int(sys.stdin.readline()))

nlist.sort()

# 출력
print(round(sum(nlist)/n))                  # 산술평균
print(nlist[n//2])                          # 정렬된 리스트에서 중앙값
n_common = Counter(nlist).most_common()     # Counter 함수로 최빈값
if len(n_common) > 1 and n_common[0][1] == n_common[1][1]:
    print(n_common[1][0])
else:
    print(n_common[0][0])
print(max(nlist) - min(nlist))



# 함수로 만들기
# def mean(number):
#     return round(sum(number)/len(number))

# def median(number):
#     center = number[len(number)//2]
#     return center

# def mode(number):
#     n_mode = Counter(number).most_common()
#     if len(number) > 1:
#         if n_mode[0][1] == n_mode[1][1]:
#             mod = n_mode[1][0]
#         else:
#             mod = n_mode[0][0]

#     return mod

# def scope(number):
#     return max(number) - min(number)

# print(mean(nlist))
# print(median(nlist))
# print(mode(nlist))
# print(scope(nlist))

# statistics 사용
# s = statistics
# print(round(s.mean(nlist)))           # 산술평균
# print(s.median(nlist)) # statistics 함수를 이용한 중앙값
