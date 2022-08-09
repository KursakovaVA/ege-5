for N in range(1,10000000):
    N = bin(N)[2:]
    w = int("1101101001111101010101",2)
    if N.count("1")%2==0:
        N += "1"
    else:
        N += "0"
    if N.count("1")%2==0:
        N += "1"
    else:
        N += "0"
    if int(N,2) > w:
        print(int(N,2))
        break