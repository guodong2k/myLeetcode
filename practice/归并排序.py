# -*- coding: utf-8 -*-
#思路：先分开，拆成最细后，两两合并。代码思路用merge_sort先递归拆分，递归尾端用merge两两合并，并且两个序列之前都排序好了的，只做合并考虑
def merge(left,right):
    res=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            res.append(left[i])
            i=i+1
        else:
            res.append(right[j])
            j=j+1
        if i==len(left):
            for a in right[j:]:
                res.append(a)
        if j==len(right):
            for b in left[i:]:
                res.append(b)
    return res

def merge_sort(a):
    if len(a)<=1:
        return a
    middle=len(a)/2
    left = merge_sort(a[:middle])
    right = merge_sort(a[middle:])
    return merge(left,right)


if __name__ == '__main__':
    a = [4, 7, 8, 3, 5, 9]
    print merge_sort(a)