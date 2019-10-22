#!/usr/bin/env python3
from random import randint

def closest_sorted (arr, x, k):
    # O(logn + k)
    # tie-breaking: choose smaller one
    if k >= len(arr):
        return arr
    # binary search and locat
    start = binary_search(arr, x, 0, len(arr)-1)
    
    # two pointer scan
    p1 = start - k + 1
    p2 = start + k
    if p1 < 0:
        p1 = 0
    if p2 > len(arr)-1:
        p2 = len(arr)-1
    while p2 - p1 + 1 > k:
        if abs(arr[p1]-x) > abs(arr[p2]-x):
            p1 += 1
        else:
            p2 -= 1
    return arr[p1:p2+1]

def binary_search (arr, x, start, end):
    # return the position of x
    pivot = (end+start)//2
    if end - start == 0 or end - start == 1:
        return start
    elif arr[pivot] == x:
        return pivot
    elif arr[pivot] < x:
        return binary_search(arr, x, pivot, end)
    elif arr[pivot] > x:
        return binary_search(arr, x, start, pivot)

def better_closest_sorted (arr, x, k):
    # O(logn + k)
    # tie-breaking: choose smaller one
    if k >= len(arr):
        return arr
    # binary search and locat
    start = binary_search(arr, x, 0, len(arr)-1)
    
    # two pointer scan
    p1 = start - k + 1  # left search boundary
    p2 = start + k  # right search boundary
    if p1 < 0:
        p1 = 0
    if p2 > len(arr)-1:
        p2 = len(arr)-1
    start = min(start, len(arr)-k)
    if start < p1:
        return arr[start:len(arr)]
    else:
        left_boundary = left_boundary_binary_search (arr, x, k, p1, start)
        right_boundary = left_boundary + k
        if left_boundary >= 0 and right_boundary < len(arr):
            return arr[left_boundary:right_boundary]
        if left_boundary < 0:
            return arr[0:right_boundary]
        if right_boundary > len(arr):
            return arr[left_boundary:len(arr)]


def left_boundary_binary_search (arr, x, k, start, end):
    length = len(arr)
    if end - start == 0:
        if start + k - 1 < length:
            return start
        else: 
            return length - k
    elif end - start == 1:
        t1 = start + k - 1
        t2 = end + k - 1
        if t1 < length:
            if t2 < length:
                # return a better one
                if abs(arr[start]-x) <= abs(arr[t2]-x):
                    return start
                else:
                    return end
            else:
                return start
        else:
            return length - k 
    # return the position of x
    l = (end+start)//2
    r = l + k - 1
    # return case check
    
    
    if l <= 1:
        l = 1
        r = l + k - 1
    elif r > len(arr) - 2:
        r = len(arr) - 2
        l = r - k
        
    # boundary check
    if abs(arr[l]-x) > abs(arr[r+1]-x):
        return left_boundary_binary_search(arr, x, k, l, start)
    elif abs(arr[l-1]-x) <= abs(arr[r]-x):
        return left_boundary_binary_search(arr, x, k, start, l)
    else:
        return l

if __name__ == '__main__':
    print(better_cloest_sorted([1,2,3,4,4,7], 5.2, 2)) # [4,4] 
    print(better_cloest_sorted([1,2,3,4,4,7], 6.5, 3)) # [4,4,7]
    print(better_cloest_sorted([1,2,3,4,4,6,6], 5, 3)) # [4,4,6] 
    print(better_cloest_sorted([1,2,3,4,4,5,6], 4, 5)) # [2,3,4,4,5]