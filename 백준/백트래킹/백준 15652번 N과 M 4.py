# n : 선택한 숫자 개수
# s : 시작할 숫자
def dfs(n, s, lst):
    if n == M:
        ans.append(lst)
        return
    # s부터 N까지 추가
    for j in range(s, N+1):
        dfs(n+1, j, lst + [j])

N, M = map(int, input().split())
ans = []
# 1부터 시작이므로 초기 s값은 1
dfs(0, 1, [])
for i in ans:
    print(*i)