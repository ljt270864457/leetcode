class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

        示例 1:

        输入: "abcabcbb"
        输出: 3
        解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
        示例 2:

        输入: "bbbbb"
        输出: 1
        解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
        示例 3:

        输入: "pwwkew"
        输出: 3
        解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。

        解题思路

        使用滑窗法解决
        1. 从第0个元素作为起始元素，依次向后遍历
        2. 内层循环从当前元素到最后一个元素，如果出现重复的元素，退出循环
        3. 计算出最大长度
        '''
        max_length = 0
        for i in range(len(s)):
            if len(s[i:]) <= max_length:
                break

            tmp_str_list = []
            for char in s[i:]:
                if char in tmp_str_list:
                    break
                tmp_str_list.append(char)

            max_length = max(len(tmp_str_list), max_length)
        return max_length


if __name__ == '__main__':
    s = 'abcabcbb'
    print(Solution().lengthOfLongestSubstring(s))
