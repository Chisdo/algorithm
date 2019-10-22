#!/usr/bin/env python3
from random import randint

def quick_select(k, arr):
    # time: O(n)
    # select the (k)th smallest number in (array)
    if arr == [] or k > len(arr) or k == 0:
        return []
    else:
        length = len(arr)
        pivot = arr[randint(0,length-1)]
        left = [x for x in arr if x < pivot]
        mid = [x for x in arr if x == pivot]
        l = len(left)
        m = len(mid)
        if k <= l:
            return quick_select(k, left)
        elif k > l and k <= l+m:
            return pivot
        else:
            r = k - l - m
            return quick_select(r, [x for x in arr if x > pivot])

if __name__ == '__main__':
    print(quick_select(2, [3,10,4,7,19])) # 4
    print(quick_select(4, [11,2,8,3])) # 