def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return
    for j in arr:
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, lst + [j])
            v[j] = 0

N, M = map(int,input().split())
arr = list(map(int, input().split()))
ans = []
v = [0] * 9999
dfs(0, [])
ans.sort()
for i in ans:
    print(*i)