# -*- coding: utf-8 -*-
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        long=len(s)
        ss=list(s)
        maxlen=0;
        i=0
        #�ӵ�һ����ĸ��ʼ�����μ��ٵ�һ����ĸ������abc��bc,c
        while i<long:
            m=ss[i:]
            #��������ַ������ӵ�һ����ʼȡ��ȡ���ظ���ĸΪֹ
            # Ȼ���ȡ���ȣ���max�����Ƚϣ�����max��ֵ��max,�ַ�����ֵ��maxstr
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
