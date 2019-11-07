#!/usr/bin/env python3
from collections import defaultdict

def topological(V, E): 
    # O(V+E)
    degree = defaultdict(lambda: 1) 
    edge = defaultdict(list) 
    # O(E)
    for elem in E:
        degree[elem[1]] += 1
        edge[elem[0]].append(elem[1])
    edge[-1] = list(range(V))
    queue = [-1]
    rs = []
    i = 0
    # O(V+E)
    while i < len(queue):
        rs.append(queue[i])
        target = edge[queue[i]]
        for elem in target:
            degree[elem] -= 1
            if degree[elem] == 0:
                queue.append(elem)
        i += 1
    if len(rs) < V:
        return None
    else:
        return rs[1:] # without sink
    
    


if __name__ == '__main__':
    print(topological(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])) # [0, 1, 2, 3, 4, 5, 6, 7]
    print(topological(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])) # [0, 1, 2, 4, 3, 5, 6, 7]
    print(topological(4, [(0,1), (1,2), (2,1), (2,3)])) # None (cycle)
    