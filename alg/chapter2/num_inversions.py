#!/usr/bin/env python3
def _num_inversions((a,num_a), (b,num_b)):
    if a == [] or b == []:
        return a + b, num_a+num_b
    else:
        rs, num = [], num_a+num_b
        i, j = 0, 0 
        i_m, j_m = len(a), len(b)
        while i < i_m and j < j_m:
            if a[i] <= b[j]:
                rs.append(a[i])
                i += 1
            elif a[i] > b[j]:
                rs.append(b[j])
                j += 1
                num += i_m - i
        if i == i_m:
            rs = rs + b[j:]
        if j == j_m:
            rs = rs + a[i:]
        return rs, num

def mid_num_inversions(lst):
    # O(nlogn)
    # calculate the number of inversions in a list
    l = len(lst)
    if l == 1:
        return lst, 0 
    return _num_inversions(mid_num_inversions(lst[:l//2]), mid_num_inversions(lst[l//2:]))

def num_inversions(lst):
    _, num = mid_num_inversions(lst)
    return num

if __name__ == '__main__':
    print(num_inversions([4,1,3,2])) # 4
    print(num_inversions([2,4,1,3])) # 3
    print(num_inversions(list(range(1000))[::-1]))
