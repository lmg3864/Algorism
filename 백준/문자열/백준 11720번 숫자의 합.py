# N : 숫자의 개수, S : N개의 숫자
N = int(input())
S = input()

sm = 0
# 숫자의 개수만큼 반복문 돌려서
# S에서의 i번째 인덱스를 sm에 더해줘서 출력
for i in range(N):
    sm += int(S[i])
print(sm)