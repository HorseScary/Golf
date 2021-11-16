for a in range(1,201):
    d=0
    for i in range(1,a):
        if a % (i)==0:
            d+=i
    if d>a:
        print(a)