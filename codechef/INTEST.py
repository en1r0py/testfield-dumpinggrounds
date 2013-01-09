import sys

l = raw_input().split()
n,k = int(l[0]), int(l[1])

data = sys.stdin.readlines()
x = 0
for each_line in data:
    t = int(each_line)
    if t%k == 0:
       x+=1
print x

