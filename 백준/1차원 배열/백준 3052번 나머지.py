import sys
sys.stdin = open("input.txt", "r")

# 입력받은 수들을 lst에 추가
lst = []
[lst.append(int(input())) for _ in range(10)]
num = []
# lst에 있는 수의 나머지들을 num에 추가
for j in lst:
    num.append(j%42)
# 중복을 제거하기위해 set을 써주고 
# num 리스트의 길이를 구해서 출력
print(len(set(num)))