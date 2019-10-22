#!/usr/bin/env python3
def merge_sorted(a, b):
    if a == [] and b == []:
        return []
    elif a == [] and b != []:
        return b
    elif a != [] and b == []:
        return a 
    else: # a and b has element
        if a[0] <= b[0]:
            return [a[0]] + merge_sorted(a[1:], b)
        else:
            return [b[0]] + merge_sorted(a, b[1:])

def merge_sort(arr):
    # time: O(nlogn)
    l = len(arr)
    if l <= 1:
        return arr
    return merge_sorted(merge_sort(arr[:l//2]), merge_sort(arr[l//2:]))


if __name__ == '__main__':
    print(merge_sort([4,2,5,1,6,3])) # [1,2,3,4,5,6]
