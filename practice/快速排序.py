# -*- coding: utf-8 -*-
#���Ҳ�Ƿ��η����㷨��ֻ��������������quick_sort��ÿ�εݹ��ֵ�ʱ�򶼻����򣬲�ֵ���ϸ��ʱ����ʵ�Ѿ�������ˣ�ֱ�Ӻϲ�����
def quick_sort(array):
    if array==[]:
        return array
    flag=array[0]
    small= quick_sort([x for x in array[1:] if x<flag])
    big = quick_sort([x for x in array[1:] if x >= flag])
    return small+[flag]+big

seq=[5,6,78,9,0,-1,2,3,-65,12]
print quick_sort(seq)