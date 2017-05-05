# -*- coding: utf-8 -*-
#˼·���ȷֿ��������ϸ�������ϲ�������˼·��merge_sort�ȵݹ��֣��ݹ�β����merge�����ϲ���������������֮ǰ��������˵ģ�ֻ���ϲ�����
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