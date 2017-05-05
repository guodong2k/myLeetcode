# -*- coding: utf-8 -*-
#思想就是两两排序，一遍一遍的码
def pop_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j]>array[j+1]:
                array[j], array[j + 1]=array[j+1],array[j]
    return array
seq=[5,6,78,9,0,-1,2,3,-65,12]
print pop_sort(seq)