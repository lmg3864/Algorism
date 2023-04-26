# n : 선택한 숫자 개수
def dfs(n, tlst):
    if n == M:
        ans.append(tlst)
        return
    # 이전에 골랐던 숫자 중복 안하기 위한 perv
    prev = 0
    for j in range(N):
        # lst에서 썼던 idx 안쓰기 위한 v
        if v[j] == 0 and prev != lst[j]:
            prev = lst[j]
            v[j] = 1
            dfs(n+1, tlst + [lst[j]])
            v[j] = 0

N, M = map(int, input().split())
lst = sorted(map(int, input().split()))
ans = []
v = [0] * N
dfs(0, [])
for i in ans:
    print(*i)