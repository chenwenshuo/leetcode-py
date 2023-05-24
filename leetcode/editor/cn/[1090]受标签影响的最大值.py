# 我们有一个 n 项的集合。给出两个整数数组 values 和 labels ，第 i 个元素的值和标签分别是 values[i] 和 labels[i]。还
# 会给出两个整数 numWanted 和 useLimit 。 
# 
#  从 n 个元素中选择一个子集 s : 
# 
#  
#  子集 s 的大小 小于或等于 numWanted 。 
#  s 中 最多 有相同标签的 useLimit 项。 
#  
# 
#  一个子集的 分数 是该子集的值之和。 
# 
#  返回子集 s 的最大 分数 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1
# 输出：9
# 解释：选出的子集是第一项，第三项和第五项。
#  
# 
#  示例 2： 
# 
#  
# 输入：values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2
# 输出：12
# 解释：选出的子集是第一项，第二项和第三项。
#  
# 
#  示例 3： 
# 
#  
# 输入：values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1
# 输出：16
# 解释：选出的子集是第一项和第四项。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == values.length == labels.length 
#  1 <= n <= 2 * 10⁴ 
#  0 <= values[i], labels[i] <= 2 * 10⁴ 
#  1 <= numWanted, useLimit <= n 
#  
# 
#  Related Topics 贪心 数组 哈希表 计数 排序 👍 58 👎 0
import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        # tem_map = dict(zip(list(i for i in range(0, len(labels))), values))
        # sort_map = dict(sorted(tem_map.items(), key=lambda x: x[1], reverse=True))
        #
        list_tem = list(zip(values, labels))
        list_tem.sort(key=lambda x: x[0], reverse=True)

        ans = 0
        map_tem = dict()

        for x in list_tem:
            if numWanted > 0:
                if x[1] not in map_tem.keys():
                    numWanted -= 1
                    ans += x[0]
                    map_tem[x[1]] = 1
                    continue
                if x[1] in map_tem.keys() and map_tem.get(x[1], 0) < useLimit:
                    map_tem[x[1]] = map_tem.get(x[1]) + 1
                    numWanted -= 1
                    ans += x[0]

        # heapq.heapify()
        # for key, value in sort_map.items():
        #     if numWanted > 0:
        #         if labels[key] not in set_key:
        #             numWanted -= 1
        #             ans += value
        #             set_key.add(labels[key])
        #             continue
        #         if labels[key] in set_key and useLimit > 1:
        #             useLimit -= 1
        #             numWanted -= 1
        #             ans += value
        return ans


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().largestValsFromLabels([4, 6, 3, 9, 2],
                                           [2, 0, 0, 0, 2], 5, 2))
