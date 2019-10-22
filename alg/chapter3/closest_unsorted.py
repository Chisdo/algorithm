#!/usr/bin/env python3
from random import randint

def cloest_unsorted (arr, x, k):
    # O(n)
    # tie-breaking: choose the earlier one
    temp = []
    # scan 1
    for i,_ in enumerate(arr):
        temp.append(abs(arr[i]-x))

    # quick select
    pivot = quick_select(k, temp)

    rs = []
    for i,_ in enumerate(temp):
        if temp[i] <= pivot and k > 0:
            rs.append(arr[i])
            k -= 1 # choose the ealier number
    return rs

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
    print(cloest_unsorted([4,1,3,2,7,4], 5.2, 2)) # [4,4] 
    print(cloest_unsorted([4,1,3,2,7,4], 6.5, 3)) # [4,7,4]
    print(cloest_unsorted([5,3,4,1,6,3], 3.5, 2)) # [3,4]
