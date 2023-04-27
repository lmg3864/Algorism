import sys
sys.stdin = open("input.txt", "r")

# N : 바구니의 총 개수, M : 바구니를 역순으로 만드는 번 수
N, M = map(int, input().split())
# 1부터 N까지 바구니 번호 lst
lst = [i for i in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    # 리스트를 i-1부터 j까지로 나눠서 temp로 지정
    # temp 뒤집어주고
    # lst 나눈 부분을 temp로 덮어 씌우기
    temp = lst[i-1:j]
    temp.reverse()
    lst[i-1:j] = temp
print(*lst)