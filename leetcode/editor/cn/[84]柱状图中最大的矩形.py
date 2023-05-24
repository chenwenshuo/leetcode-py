# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。 
# 
#  求在该柱状图中，能够勾勒出来的矩形的最大面积。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入： heights = [2,4]
# 输出： 4 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= heights.length <=10⁵ 
#  0 <= heights[i] <= 10⁴ 
#  
# 
#  Related Topics 栈 数组 单调栈 👍 2423 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        if all(i == 1 for i in heights):
            return len(heights)
        for i in range(0, len(heights)):
            tem_min = heights[i]
            for j in range(i, len(heights)):
                tem_min = min(tem_min, heights[j])
                ans = max(tem_min * (j - i + 1), ans)
        return ans


if __name__ == '__main__':
    print(Solution.largestRectangleArea(None, [2, 1, 5, 6, 2, 3]))
# leetcode submit region end(Prohibit modification and deletion)
