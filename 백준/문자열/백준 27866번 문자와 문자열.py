import sys
sys.stdin = open("input.txt", "r")

st = input()
idx = int(input())
# st에서 입력받은 수 - 1 (idex는 0부터이므로)번째 값 출력
print(st[idx-1])