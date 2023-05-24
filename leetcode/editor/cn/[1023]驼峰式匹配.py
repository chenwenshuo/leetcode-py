# 如果我们可以将小写字母插入模式串 pattern 得到待查询项 query，那么待查询项与给定模式串匹配。（我们可以在任何位置插入每个字符，也可以插入 0 
# 个字符。） 
# 
#  给定待查询列表 queries，和模式串 pattern，返回由布尔值组成的答案列表 answer。只有在待查项 queries[i] 与模式串 
# pattern 匹配时， answer[i] 才为 true，否则为 false。 
# 
#  
# 
#  示例 1： 
# 
#  输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
# , pattern = "FB"
# 输出：[true,false,true,true,false]
# 示例：
# "FooBar" 可以这样生成："F" + "oo" + "B" + "ar"。
# "FootBall" 可以这样生成："F" + "oot" + "B" + "all".
# "FrameBuffer" 可以这样生成："F" + "rame" + "B" + "uffer". 
# 
#  示例 2： 
# 
#  输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
# , pattern = "FoBa"
# 输出：[true,false,true,false,false]
# 解释：
# "FooBar" 可以这样生成："Fo" + "o" + "Ba" + "r".
# "FootBall" 可以这样生成："Fo" + "ot" + "Ba" + "ll".
#  
# 
#  示例 3： 
# 
#  输出：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
# , pattern = "FoBaT"
# 输入：[false,true,false,false,false]
# 解释： 
# "FooBarTest" 可以这样生成："Fo" + "o" + "Ba" + "r" + "T" + "est".
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= queries.length <= 100 
#  1 <= queries[i].length <= 100 
#  1 <= pattern.length <= 100 
#  所有字符串都仅由大写和小写英文字母组成。 
#  
# 
#  Related Topics 字典树 双指针 字符串 字符串匹配 👍 83 👎 0
import bisect
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)

if __name__ == "__main__":
    lst = []
    lst1 = list()
    list2 = [x ** 2 for x in range(10)]
    list2.sort()
    list2.reverse()
    print(list2.pop())
    list2.append(0)
    print(list2.index(0))
    list2.insert(10, 9)
    print(list2)


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = list()
        for q in queries:
            flag = isPattern(q, pattern)
            ans.append(flag)
        return ans


def isPattern(q, pattern):
    a = 0
    b = 0
    while a < len(q) and b < len(pattern):
        if q[a] == pattern[b]:
            a += 1
            b += 1
            continue
        if q[a].islower() and q[a] != pattern[b]:
            a += 1
            continue
        return False
    if a < len(q):
        for s in q[a:]:
            if s.isupper():
                return False
    if b < len(pattern):
        return False
    return True


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        lst = [3, 5, 7]
        ans = 0
        for i in range(1, n + 1):
            for tem in lst:
                if n / tem == 0:
                    ans = ans + i
                    break
        return ans

# leetcode submit region end(Prohibit modification and deletion)


# 6390.
# 滑动子数组的美丽值
#
# 示例
# 1：
#
# 输入：nums = [1, -1, -3, -2, 3], k = 3, x = 2
# 输出：[-1, -2, -2]
# 解释：总共有
# 3
# 个
# k = 3
# 的子数组。
# 第一个子数组是[1, -1, -3] ，第二小的数是负数 - 1 。
# 第二个子数组是[-1, -3, -2] ，第二小的数是负数 - 2 。
# 第三个子数组是[-3, -2, 3] ，第二小的数是负数 - 2 。
# 示例
# 2：
#
# 输入：nums = [-1, -2, -3, -4, -5], k = 2, x = 2
# 输出：[-1, -2, -3, -4]
# 解释：总共有
# 4
# 个
# k = 2
# 的子数组。
# [-1, -2]
# 中第二小的数是负数 - 1 。
# [-2, -3]
# 中第二小的数是负数 - 2 。
# [-3, -4]
# 中第二小的数是负数 - 3 。
# [-4, -5]
# 中第二小的数是负数 - 4 。
# 示例
# 3：
#
# 输入：nums = [-3, 1, 2, -3, 0, -3], k = 2, x = 1
# 输出：[-3, 0, -3, -3, -3]
# 解释：总共有
# 5
# 个
# k = 2
# 的子数组。
# [-3, 1]
# 中最小的数是负数 - 3 。
# [1, 2]
# 中最小的数不是负数，所以美丽值为
# 0 。
# [2, -3]
# 中最小的数是负数 - 3 。
# [-3, 0]
# 中最小的数是负数 - 3 。
# [0, -3]
# 中最小的数是负数 - 3 。
#
#
# 提示：
#
# n == nums.length
# 1 <= n <= 105
# 1 <= k <= n
# 1 <= x <= k
# -50 <= nums[i] <= 50
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        # write your code here
        ans = []
        lst = sorted(nums[:k])
        for i in range(k-1, len(nums)):
            if i >= k:
                remove_index = bisect.bisect_left(lst, nums[i - k])
                lst.pop(remove_index)
                bisect.insort_left(lst, nums[i])
            #
            # lst.sort()
            if lst[x - 1] < 0:
                ans.append(lst[x - 1])
            else:
                ans.append(0)
        return ans


sol = Solution()
print(sol.getSubarrayBeauty([1, -1, -3, -2, 3], 3, 2))