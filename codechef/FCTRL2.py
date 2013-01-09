n = int(raw_input())
for i in range(n):
    x = int(raw_input())
    f = 1
    while x > 1:
        f = f*x
        x-=1
    print f
