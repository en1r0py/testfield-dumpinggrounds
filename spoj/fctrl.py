c = int(raw_input())

for i in range(c):
    f = 0
    x = int(raw_input())
    while x >= 5:
        x/=5
        f+=x
    print f


