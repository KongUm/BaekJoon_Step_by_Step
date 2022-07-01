N = int(input())
ans = 1

def fac(N, ans):
    if N <= 1:
        print(ans)
        return
    ans = N * ans
    N = N - 1
    fac(N, ans)

fac(N, ans)