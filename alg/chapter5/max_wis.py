#!/usr/bin/env python3
import heapq

def max_wis(lst):
    # O(n)
    if lst == []:
        return 0
    dic = {}
    dic[0] = 0
    dic[1] = 0
    for i in range(2, len(lst)+2):
        dic[i] = max (dic[i-2]+lst[i-2], dic[i-1])
    return dic[len(lst)+1]
    
if __name__ == '__main__':
    print(max_wis([7,8,5])) # (12, [7,5])
    print(max_wis([-1,8,10])) # (10, [10])
    print(max_wis([])) # (0, [])
    print(max_wis([-5,-1,-4]))
