# 编写一个函数来查找字符串数组中的最长公共前缀。 
# 
#  如果不存在公共前缀，返回空字符串 ""。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
#  
# 
#  示例 2： 
# 
#  
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= strs.length <= 200 
#  0 <= strs[i].length <= 200 
#  strs[i] 仅由小写英文字母组成 
#  
# 
#  Related Topics 字典树 字符串 👍 2776 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        for n in zip(*strs):
            if all(e == n[0] for e in n):
                ans += n[0]
            else:
                return ans
        return ans


if __name__ == '__main__':
    print(Solution.longestCommonPrefix(None,
                                       ["flower", "flow", "flight"]))
# leetcode submit region end(Prohibit modification and deletion)
