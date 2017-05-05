# -*- coding: utf-8 -*-
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        long=len(s)
        ss=list(s)
        maxlen=0;
        i=0
        #从第一个字母开始，依次减少第一个字母，比如abc，bc,c
        while i<long:
            m=ss[i:]
            #遍历这个字符串，从第一个开始取，取到重复字母为止
            # 然后获取长度，和max变量比较，大于max则赋值给max,字符串赋值给maxstr
            str = ''
            for j in m:
                if str.find(j)== -1:
                    str=str+j
                else:
                    break
            if len(str) > maxlen:
                maxlen = len(str)
            i=i+maxlen-1
        return maxlen
