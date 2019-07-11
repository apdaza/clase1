def comparar(l1,l2):
    p = 0
    f = 0
    for i in range(len(l1)):
        if l1[i] in l2:
            if l1[i] == l2[i]:
                f += 1
            else:
                p += 1
    return f,p
