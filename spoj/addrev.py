if __name__ == "__main__":
    c = int(raw_input())

    for i in range(c):
        s1,s2 = raw_input().split()
        n = int(s1[::-1]) + int(s2[::-1])
        s_nrev = str(n)[::-1]
        print int(s_nrev)





