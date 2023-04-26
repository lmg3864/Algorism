# n : 고른 숫자 개수
def dfs(n, tlst):
    if n == M:
        ans.append(tlst)
        return
    for j in range(len(lst)):
        dfs(n+1, tlst + [lst[j]])

N, M = map(int, input().split())
lst = sorted(map(int, input().split()))
ans = []
dfs(0, [])
for i in ans:
    print(*i)