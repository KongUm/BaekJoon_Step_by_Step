N = int(input())
a = N
t = 0

while a != 1:
    a = a//3
    t = t+1
t = t-1


cp = [['*']*N for _ in range(N)]
def star(N,t):
    if t < 0:
        print(cp)
        return 
    b = (N-1)//2
    c = ((3**t)-1)//2
    print(t,b,c)
    cp[b-c:b+c+1][b-c:b+c+1] = ' '
    star(N,t-1)


star(N,t)
 