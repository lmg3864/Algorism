# n : 고른 숫자 개수
def dfs(n, s, tlst):
    if n == 6:
        ans.append(tlst)
        return
    for j in range(s, N):
        dfs(n+1, j+1, tlst + [lst[j]])

# 마지막에 0을 준다고 하였으므로
# while문에 조건문을 넣어서 구성
while True:
    before_lst = list(map(int, input().split()))
    if before_lst[0] == 0:
        break
    # 리스트 슬라이싱
    N = before_lst[0]
    lst = before_lst[1:]
    ans = []
    dfs(0, 0, [])
    for i in ans:
        print(*i)
    print()