#!/usr/bin/env python3
from collections import defaultdict
thePair = set()
thePair.add('AU')
thePair.add('UA')
thePair.add('CG')
thePair.add('GC')
thePair.add('UG')
thePair.add('GU')

def isPair(a,b,rna):
    return rna[a]+rna[b] in thePair

    
def best(s):
    opt = defaultdict(int)
    back = defaultdict(int)
    n = len(s)
    # l=1
    for i in range(n-1):
        j = i+1
        if isPair(i,j,s):
            opt[i,j] = 1
            back[i,j] = i,j
        else:
            back[i,j] = -1,-1
        
    # l>1
    for l in range(2, n): # 0,1 for base case?
        for i in range(0, n-l):
            j = i+l 
            for k in range(i+1, j+1):
                if isPair(i,k,s):
                    temp = opt[i+1,k-1]+opt[k+1,j]+1
                    if temp > opt[i,j]:
                        opt[i,j] = temp
                        back[i,j] = i,k
                else:
                    temp = opt[i+1,j]
                    if temp > opt[i,j]:
                        opt[i,j] = temp
                        back[i,j] = -1,-1
    i,j = 0,n-1
    rs = ''
    print(back)
    def sol(m,n):
        if m==n: # only one element
            return '.'
        if m > n or (m,n) not in back:
            return ''
        if back[m,n] == (-1,-1):
            return '.' + sol(m+1,n)
        else:
            x, y = back[m,n] 
            return '(' + sol(x+1,y-1) + ')' + sol(y+1,n)

    return opt[0,n-1], sol(i,j)

def total(s):
    opt = defaultdict(lambda: 1)
    n = len(s)
    for i in range(n-1):
        j = i+1
        if isPair(i,j,s):
            opt[i,j] = 2
        else:
            opt[i,j] = 1
    for l in range(2,n):
        for i in range(0,n-l):
            j = i + l
            opt[i,j] = 1*opt[i+1,j]
            for k in range(i+1,j+1):
                if isPair(i,k,s):
                    opt[i,j] += 1*opt[i+1,k-1]*opt[k+1,j]
    return opt[0,n-1]

if __name__ == '__main__':
    #print(best('CCCGGG')) # 3
    #print(best('ACAGU'))
    # (2, '((.))')
    print(total('ACAGU'))
    # 6
    #print(best('UUCAGGA'))
    # (3, '(((.)))')
    print(total('UUCAGGA'))
    # 24
    #print(best('GAUGCCGUGUAGUCCAAAGACUUC'))
    # (11, '(((()()((()(.))))((.))))')
    print(total('GAUGCCGUGUAGUCCAAAGACUUC'))
    # 2977987
