def digitsProduct(n):
    if n < 10:
        if n == 0:
            return 10
        return n
    l = []
    def rF(n):
        digits = range(9,1,-1)
        if n in digits:
            l.append(n)
            return None 
        for i in digits:
            if n%i == 0:
                l.append(i)
                break
            if i == 2 and n%i != 0:
                l.append(-1)
                return None
        return rF(n/i)
    rF(n)
    if -1 in l:
        return -1
    l.reverse()
    s= ''
    for i in l:
        s+= str(i)
    
    return int(s)

print digitsProduct(9)