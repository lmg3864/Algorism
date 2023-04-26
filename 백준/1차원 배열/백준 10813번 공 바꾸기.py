import sys
sys.stdin = open("input.txt", "r")

# N : 바구니의 개수, M : 공 바꾸는 횟수
N, M = map(int, input().split())
# 빈 리스트 lst를 만들어서 반복문 돌려서 자기 idx보다 1크게 넣어줌
lst = []
for i in range(N):
    lst.append(i+1)
# i, j 번째에 들어있는 공을 바꾸기 위해서 idx이므로 1씩 빼주고 서로 자리 교환
for _ in range(M):
    i, j = map(int, input().split())
    lst[i-1], lst[j-1] = lst[j-1], lst[i-1]
print(*lst)