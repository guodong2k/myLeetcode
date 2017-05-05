# -*- coding: utf-8 -*-
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        list=str.split(' ')
        print list
        if len(list) != len(pattern):
            return False
        dict={}
        mapval = {}
        for i in range(len(pattern)):
            if pattern[i:i+1] in dict:
                print pattern[i:i+1],list[i]
                if dict[pattern[i:i+1]]==list[i]:
                    continue
                else:
                    return False
            else:
                if list[i] in mapval:
                    return False
                dict[pattern[i:i+1]]=list[i]
                mapval[list[i]] = True

        return True



s=Solution()
pattern = "abba"
str = "dog cat cat dog"
print s.wordPattern(pattern, str)