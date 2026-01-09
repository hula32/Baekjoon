# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

# 5
# 20 10 35 30 7

# 7 35

N = int(input())
number = list(map(int, input().split()))

min_val = min(number)
max_val = max(number)

print(min_val, max_val)