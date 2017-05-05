# -*- coding: utf-8 -*-
#这个也是分治法的算法，只不过他把排序在quick_sort中每次递归拆分的时候都会排序，拆分到最细的时候其实已经排序好了，直接合并即可
def quick_sort(array):
    if array==[]:
        return array
    flag=array[0]
    small= quick_sort([x for x in array[1:] if x<flag])
    big = quick_sort([x for x in array[1:] if x >= flag])
    return small+[flag]+big

seq=[5,6,78,9,0,-1,2,3,-65,12]
print quick_sort(seq)