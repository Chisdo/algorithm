#!/usr/bin/env python3
import heapq

def unbounded(w, lst):
    # O(nw)
    dic = {}
    backtrack = {}
    dic[0] = 0
    backtrack[0] = -1
    for i in range(1, w+1):
        dic[i] = dic[i-1]
        backtrack[i] = -1
        for j in range(len(lst)):
            w_j,v_j = lst[j]
            if i >= w_j:
                temp = dic[i-w_j]+v_j
                if temp > dic[i]:
                    dic[i] = temp
                    backtrack[i] = j

    # organize
    x = w
    rs = [0 for i in range(len(lst))]
    while x > 0:
        if backtrack[x] == -1:
            x -= 1
        else:
            rs[backtrack[x]] += 1
            x -= lst[backtrack[x]][0]
    return dic[w], rs
if __name__ == '__main__':
    # (weight, list of [(weight, value)])
    print(unbounded(3, [(2, 4), (3, 5)])) # (5, [0, 1])
    print(unbounded(3, [(1, 5), (1, 5)])) # (15, [3, 0])
    print(unbounded(3, [(1, 2), (1, 5)])) # (15, [0, 3])
    print(unbounded(3, [(1, 2), (2, 5)])) # (7, [1, 1])
    print(unbounded(58, [(5, 9), (9, 18), (6, 12)])) # (114, [2, 4, 2])
    print(unbounded(92, [(8, 9), (9, 10), (10, 12), (5, 6)])) # (109, [1, 1, 7, 1])
    