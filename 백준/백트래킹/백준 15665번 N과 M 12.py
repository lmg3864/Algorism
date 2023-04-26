# n : 선택한 숫자 개수
def dfs(n, s, tlst):
    if n == M:
        ans.append(tlst)
        return
    # 이전에 골랐던 숫자 중복 안하기 위한 perv
    prev = 0
    for j in range(s, N):
        if prev != lst[j]:
            prev = lst[j]
            dfs(n+1, j, tlst + [lst[j]])

N, M = map(int, input().split())
lst = sorted(map(int, input().split()))
ans = []
dfs(0, 0, [])
for i in ans:
    print(*i)