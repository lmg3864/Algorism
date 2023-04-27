import sys
sys.stdin = open("input.txt", "r")

N = int(input())
lst = list(map(int, input().split()))
# mx : 최고점
mx = max(lst)
ans = []
for i in lst:
    # ans에 계산된 값 추가
    ans.append(i/mx*100)
# ans 평균 구해서 출력
print(sum(ans)/len(ans))