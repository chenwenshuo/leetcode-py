# 给定 m x n 矩阵 matrix 。 
# 
#  你可以从中选出任意数量的列并翻转其上的 每个 单元格。（即翻转后，单元格的值从 0 变成 1，或者从 1 变为 0 。） 
# 
#  返回 经过一些翻转后，行与行之间所有值都相等的最大行数 。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[0,1],[1,1]]
# 输出：1
# 解释：不进行翻转，有 1 行所有值都相等。
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[0,1],[1,0]]
# 输出：2
# 解释：翻转第一列的值之后，这两行都由相等的值组成。
#  
# 
#  示例 3： 
# 
#  
# 输入：matrix = [[0,0,0],[0,0,1],[1,1,0]]
# 输出：2
# 解释：翻转前两列的值之后，后两行由相等的值组成。 
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 300 
#  matrix[i][j] == 0 或 1 
#  
# 
#  Related Topics 数组 哈希表 矩阵 👍 97 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        map_t = {}

        for line in matrix:
            x = y = ''
            for i, n in enumerate(line):
                if n == 0:
                    x += str(i)
                else:
                    y += str(i)
            map_t[x] = map_t.get(x, 0) + 1
            map_t[y] = map_t.get(y, 0) + 1

        return max(map_t.values())

        # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution.maxEqualRowsAfterFlips(None, [[0, 0, 0], [0, 0, 1], [0, 0, 1]]))
2