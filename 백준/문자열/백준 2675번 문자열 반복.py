T = int(input())
for _ in range(T):
    R, S = input().split()
    # 숫자는 int 처리
    R = int(R)
    ans = []
    # 반복문 이용해서 문자열 차례대로 R씩 곱하기
    for i in S:
        ans.append(i*R)
    # join 이용하여 붙여주기
    print(''.join(ans))