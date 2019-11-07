#!/usr/bin/env python3
import heapq
from collections import defaultdict

def bounded(w, lst):
    # O(nW')
    dic = defaultdict(int) # dic[(0,1-n)] = 0
    back = defaultdict(int)
    n = len(lst)
    for i in range(1, w+1):
        for j in range(n):
            w_j,v_j,c_j = lst[j]
            for k in range(c_j+1):
                if i < k*w_j:
                    break
                else:
                    temp = dic[(i-k*w_j,j-1)] + k*v_j
                    if temp > dic[(i,j)]:
                        dic[(i,j)] = temp
                        back[(i,j)] = (j,k,(i-k*w_j,j-1))
    rs = [0 for i in range(n)]
    i,j = w,n-1
    while back[i,j][2][0]>0: # either weight is > 0 (when having more weight)
        bag_j, bag_k, (i,j) = back[i,j]
        rs[bag_j] += bag_k
        if j == -1:
            break
    if j != -1: # (no enough weight)
        bag_j, bag_k, (i,j) = back[i,j]
        rs[bag_j] += bag_k
    return dic[(w,n-1)], rs    
if __name__ == '__main__':
    print(bounded(3, [(2, 4, 2), (3, 5, 3)])) # (5, [0, 1])
    print(bounded(3, [(1, 5, 2), (1, 5, 3)])) # (15, [2, 1])
    print(bounded(3, [(1, 5, 1), (1, 5, 3)])) # (15, [1, 2])
    print(bounded(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)])) # (130, [6, 4, 1])
    print(bounded(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)])) # (236, [6, 7, 3, 7, 2])

