import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for _ in range(T):
    st = input()
    ans = []
    # st의 앞 글자와 뒷 글자를 출력하라고 하였으모 
    # idex로 접근해서 ans에 추가해서
    # join 사용해서 결과 출력
    ans.append(st[0])
    ans.append(st[-1])
    print(''.join(ans))