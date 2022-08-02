for N in range(1,1000000000):
    N = oct(n)[2:]
    SUM = 0
    for i in N:
        SUM += int(i)
    SUM = bin(SUM)[2:]
    if SUM == SUM[::-1]:
        SUM += "1"
    else:
        SUM += "0"
    r = int(SUM,2)
    if r > 80:
        print(r)
        break