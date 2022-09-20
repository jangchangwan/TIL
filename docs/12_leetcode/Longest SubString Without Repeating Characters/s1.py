# 가장 긴 문자열 찾기
# 2022-08-21


class Solution:
    def lengthOfLongestSubstring(self, string):

        string_dic = dict()

        for s in string:
            if string_dic.get(s):
                string_dic[s] += 1
            else:
                string_dic[s] = 1

        print(string_dic)
