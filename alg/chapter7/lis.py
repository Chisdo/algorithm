#!/usr/bin/env python3
import heapq

def lis(s): 
    # Longest Increasing Subsequence
    # O(n^2) 
    if s == '':
        return ''
    else:
        a = list(map(ord, s)) + [float('inf')] # convert chars to ints and add dummy sink
        l = len(a)
        opt = {} # return the lis of current sequence lengths
        back = {}
        opt[0] = 1 # base case, the first element itself
        back[0] = -1
        for i in range(1,l):
            opt[i] = opt[i-1]
            back[i] = -2
            for j in range(i):
                if a[j] < a[i] and opt[j]+1 > opt[i]:
                    opt[i] = opt[j]+1
                    back[i] = j
        rs = ''
        l = l-1
        while back[l] != -1:
            if back[l] != -2:
                rs = s[back[l]] + rs
                l = back[l]
            else: # == -2: find previous one
                l = l-1
        return rs


if __name__ == '__main__':
    print(lis('aebbcg')) # abcg
    print(lis('zyx')) # z
    print(lis('zadbc')) # abc
    print(lis('acdb')) # acd
    from time import time
    from random import randint
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = ''
    for i in range(20000):
        b += a[randint(0,25)]
    t = time()
    lis(b)
    print(time()-t)