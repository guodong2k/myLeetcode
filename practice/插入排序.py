# -*- coding: utf-8 -*-
#这是一个嵌套循环，从第二个开始往前一个一个比，如果比前一个元素小，上升，然后从第三个开始往前一个一个比，第四个一个一个往前比，前面的数字是已经排序好的
array = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5,5,5]

def insert_sort(a):
    list=a
    for i in range(1,len(list)):
        key=list[i]
        print key
        j=i-1
        while j>=0:
            if list[j]>key:
                list.pop(j+1)
                list.insert(j,key)
            j=j-1
    return list
print insert_sort(array)