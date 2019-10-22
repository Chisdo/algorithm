#!/usr/bin/env python3
from random import randint
import heapq

def get_smallest_pairs_a(a,b):
    # O(n^2logn)
    # enumerate all n^2 pairs
    # tie-breaking: x from a, y from b, (x+y ==x'+y', y<y')

    # O(nlogn)
    a.sort()
    b.sort()
    # O(n^2)
    c = [((x+y,y), (x,y)) for x in a for y in b]
    # O(n^2logn)
    c.sort()
    # O(n)
    rs = []
    for i in range(len(a)):
        rs.append(c[i][1])
    return rs

def get_smallest_pairs_b(a,b):
    # O(n^2logn)
    # enumerate all n^2 pairs
    # tie-breaking: x from a, y from b, (x+y ==x'+y', y<y')

    # O(nlogn)
    a.sort()
    b.sort()
    # O(n^2)
    c = [((x+y,y), (x,y)) for x in a for y in b]
    # O(n^2) of finding pivot
    pivot = quick_select(len(a),c)
    # O(n^2)
    temp_rs = [x for x in c if x <= pivot]
    # O(n)
    rs = [x for (_,x) in sorted(temp_rs)]
    return rs

def quick_select(k, arr):
    # time: O(n^2)
    # select the (k)th smallest number in (array)
    if arr == [] or k > len(arr) or k == 0:
        return None
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
    
def get_smallest_pairs_c(a,b):
    # O(nlogn)
    # enumerate n pairs
    # tie-breaking: x from a, y from b, (x+y ==x'+y', y<y')

    # O(nlogn)
    a.sort()
    b.sort()

    used = set()
    item = ((a[0]+b[0], b[0]), (0,0))
    used.add((0,0))
    heap = [item]
    rs = []
    while len(rs) < len(a):
        # pop the heap
        item = heapq.heappop(heap)
        # add to result
        rs.append(item)
        _, (x,y) = item
        # add used set
        used.add((x,y))
        # add new elements to heap
        if (x+1, y) not in used and x+1 < len(a):
            item = ((a[x+1]+b[y],b[y]),(x+1,y))
            heapq.heappush(heap, item)
        if (x, y+1) not in used and y+1 < len(a):
            item = ((a[x]+b[y+1],b[y+1]),(x,y+1))
            heapq.heappush(heap, item)
    return [(a[x],b[y]) for (_,(x,y)) in rs]


if __name__ == '__main__':
    a, b = [4,1,5,3], [2,6,3,4] # [1,3,4,5], [2,3,4,6]
    print(get_smallest_pairs_a(a,b)) # [(1,2),(1,3),(3,2),(1,4)]
    print(get_smallest_pairs_b(a,b)) # [(1,2),(1,3),(3,2),(1,4)]
    print(get_smallest_pairs_c(a,b)) # [(1,2),(1,3),(3,2),(1,4)]

    