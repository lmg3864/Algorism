import sys
sys.stdin = open("input.txt", "r")

# inpur_lst : 입력받은 값을 저장할 list
input_lst = []
for i in range(28):
    input_lst.append(int(input()))

# lst : 1부터 30까지의 수를 저장할 list
lst = [i for i in range(1, 31)]
ans = []
# lst를 순회하면서 값들이 input_lst에 있는지 체크하고
# 없으면 그 수를 ans에 추가
for j in lst:
    if j not in input_lst:
        ans.append(j)
for k in ans:
    print(k)