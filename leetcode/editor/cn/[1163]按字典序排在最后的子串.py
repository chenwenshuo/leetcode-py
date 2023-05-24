# 给你一个字符串 s ，找出它的所有子串并按字典序排列，返回排在最后的那个子串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abab"
# 输出："bab"
# 解释：我们可以找出 7 个子串 ["a", "ab", "aba", "abab", "b", "ba", "bab"]。按字典序排在最后的子串是 
# "bab"。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "leetcode"
# 输出："tcode"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 4 * 10⁵ 
#  s 仅含有小写英文字符。 
#  
# 
#  Related Topics 双指针 字符串 👍 156 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # abcdba
    def lastSubstring(self, s: str) -> str:
        return max(s[:i] for i in range(len(s)))
# leetcode submit region end(Prohibit modification and deletion)
