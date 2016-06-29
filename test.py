for i in range(5):
    l=[1,2,3,4,5]
    l.append(1024)
    l.append(255)
    del l[3]
    print l[i+1]