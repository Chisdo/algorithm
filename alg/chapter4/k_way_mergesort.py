#!/usr/bin/env python3
from heapq import merge
def k_way_merge_sort(arr, k):
    l = len(arr)
    if l <= 1:
        return arr
    split = (l-1)//k + 1
    rs = [k_way_merge_sort(arr[i:i+split],k) for i in range(0,l,split)]
    return list(merge(*rs))
    
if __name__ == '__main__':
    print(k_way_merge_sort([4,1,5,2,6,3,7,0], 3)) # [1,2,3,4,5,6]
