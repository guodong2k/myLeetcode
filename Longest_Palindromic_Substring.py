# -*- coding: utf-8 -*-
class Solution(object):
    def longestPalindrome(self, s):
        if len(s)==1:
            return s
        i=0
        maxlen=0;
        maxstr=''
        ss=list(s)
        res=[]
        while i<=len(ss):
            j=0
            while j<=len(ss):
                if j<i:
                    pass
                else:
                    string=ss[i:j]
                    if  string==self.ispalindromic(string):
                        if len(string)>maxlen:
                            maxlen=len(string)
                            maxstr=string
                j=j+1
            i=i+1
        if maxstr==[] or maxstr is None or maxstr=='':
            return s[0:1]
        return ''.join(maxstr)
    #判断是否回文
    def ispalindromic(self,list):
        #把list倒叙一下
        i=1
        reslist = []
        while abs(i)<len(list):
            i = i - 1
            if i==0:
                s= list[i-1:]
            else:
                s= list[i-1:i]
            reslist=reslist+s
        return reslist