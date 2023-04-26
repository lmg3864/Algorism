# n : 고른 숫자 개수
# 비 내림차순 이므로 시작하는 곳 s
def dfs(n, s, tlst):
    if n == M:
        ans.append(tlst)
        return
    for j in range(s, N):
        dfs(n+1, j, tlst + [lst[j]])

N, M = map(int, input().split())
lst = sorted(map(int, input().split()))
ans = []
dfs(0, 0, [])
for i in ans:
    print(*i)