def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return
    for j in range(1, N+1):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, lst + [j])
            v[j] = 0

N, M = map(int, input().split())
v=[0] * (N+1)
ans = []
dfs(0, [])
for i in ans:
    print(*i)