# n : lst의 index, cnt : 모음의 개수, tlst : 완성된 비밀번호 문자열
def dfs(n, cnt, tlst):
    if n==C:
        if len(tlst) == L and cnt >= 1 and L-cnt >= 2:
            ans.append(tlst)
        return
    dfs(n+1, cnt+tbl[ord(lst[n])], tlst + lst[n])
    dfs(n+1, cnt, tlst)

L, C = map(int, input().split())
lst = sorted(input().split())

# Lookup table (모음인 경우 1, 그 이외 0)
tbl = [0] * 128
for st in "aeiou":
    tbl[ord(st)] = 1

ans = []
dfs(0, 0, "")

for i in ans:
    print(i)