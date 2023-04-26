# n : 선택한 숫자 수, s : 시작 j위치
def dfs(n, s, tlst):
    if n == M:
        ans.append(tlst)
        return

    # 오름차순으로 정렬이기 때문에 선택한 수 보다 큰 숫자를 다음에 선택해주기
    for j in range(s, N):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, j+1, tlst + [lst[j]])
            v[j] = 0

N, M = map(int, input().split())
lst = sorted(map(int, input().split()))
ans = []
v = [0] * N
dfs(0, 0, [])
for i in ans:
    print(*i)