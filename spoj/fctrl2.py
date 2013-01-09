def fact(x):
    f = 1
    for i in range(2,x+1):
        f *= i
    return f

c = int(raw_input())
for i in range(c):
     print fact(int(raw_input()))


