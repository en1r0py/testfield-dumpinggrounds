soe = []

def generate_sieve(n):
    l = range(0,n+1)
    for i in l:
        if i == 0 or i == 1:
            l[i] = 0
            continue
        j = i + i
        while j < len(l):
            l[j] = 0
            j+=i

    global soe
    for i in l:
        if i!=0:
            soe.append(i)
    return soe

def primes_in_between(min_r, max_r):
    min_index = 0
    max_index = len(soe) - 1

    while soe[min_index] < min_r and min_index < len(soe):
        min_index+=1

    while soe[max_index] > max_r and max_index > -1:
        max_index-=1

    return soe[min_index:max_index+1]


def spoj_code():
    count = int(raw_input())
    l = []

    for i in range(count):
        s1,s2 = raw_input().split()
        r1,r2 = int(s1), int(s2)
        l.append((r1,r2))

    generate_sieve(1000)

    for (each_min_r, each_max_r) in l:
        prime_list = primes_in_between(each_min_r, each_max_r)

        for x in prime_list:
            print x

        print ""

if __name__ == "__main__":
    spoj_code()



