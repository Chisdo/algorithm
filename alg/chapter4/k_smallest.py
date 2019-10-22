#!/usr/bin/env python3
import heapq

def k_smallest(k, stream):
    heap = []
    # O(nlogk)
    for i, elem in enumerate(stream):
        elem = -elem
        if i<k:
            heapq.heappush(heap, elem)
        else: # i>=k
            if elem > heap[0]:
                heapq.heapreplace(heap, elem)
    return sorted([-x for x in heap])
    
if __name__ == '__main__':
    print(k_smallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7])) # [2, 3, 5, 7]
