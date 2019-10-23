#!/usr/bin/env python3
import heapq

def num_no(n):
    # O(n)
    dic = {}
    dic[0] = 0
    dic[1] = 2
    dic[2] = 3
    for i in range(3,n+1):
        dic[i] = dic[i-1]+dic[i-2]
    return dic[n]

def num_yes(n):
    return pow(2,n)-num_no(n)



if __name__ == '__main__':
    print(num_no(3)) # 5
    print(num_yes(3)) # 3
    
