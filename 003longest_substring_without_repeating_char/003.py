# 滑动窗口版本

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        sub_set = set()
        i=j=0
        ans = 0
        while(i<n and j<n):
            if(s[j] not in sub_set):  # 搞不明白 大大断点就明白了
                sub_set.add(s[j])
                j += 1
                ans = max(ans, j-i)
            else:
                sub_set.remove(s[i])
                i+=1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))