#!/usr/bin/env python3



def _longest_path(tree):
    # O(n)
    #return _longest_path(l) + _longest_path(root) + _longest_path(r)
    if tree == []:
        return 0, 0
    depth_left, total_left = _longest_path(tree[0])
    depth_right, total_right = _longest_path(tree[2])
    return max(depth_left, depth_right)+1, max(total_left, total_right, depth_left + depth_right)

def longest_path(tree):
    _, rs = _longest_path(tree)
    return rs

if __name__ == '__main__':
    print(longest_path([[], 1, []])) # 0
    print(longest_path([[[],1,[]], 2, [[],3,[]]])) # 2
    print(longest_path([[[[],1,[]], 2, [[],3,[]]], 4, [[[],5,[]], 6, [[],7,[[],9,[]]]]])) # 5
