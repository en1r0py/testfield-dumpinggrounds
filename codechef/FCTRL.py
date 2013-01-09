n = int(raw_input())
for i in range(n):
    x = int(raw_input())
    s = 0
    while x > 0:
        x = x/5
        s += x
    print s
