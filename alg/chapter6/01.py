#!/usr/bin/env python3
import heapq

def num_bsts(n):
    # O(n^2)
    # Catalan number
    dic = {}
    dic[0] = 1
    dic[1] = 1
    dic[2] = 2
    for i in range(3, n+1):
        dic[i] = 0
        for j in range(i):
            left = dic[j]
            right = dic[i-1-j]
            dic[i] += left*right
    return dic[n]
    
if __name__ == '__main__':
    print(num_bsts(2)) # 2
    print(num_bsts(3)) # 5
    print(num_bsts(5)) # 42

