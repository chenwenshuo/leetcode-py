# 
#  
#  给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true ；否则
# ，返回 false 。 
#  
#  
# 
#  二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [3,4,5,1,2], subRoot = [4,1,2]
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  root 树上的节点数量范围是 [1, 2000] 
#  subRoot 树上的节点数量范围是 [1, 1000] 
#  -10⁴ <= root.val <= 10⁴ 
#  -10⁴ <= subRoot.val <= 10⁴ 
#  
# 
#  Related Topics 树 深度优先搜索 二叉树 字符串匹配 哈希函数 👍 912 👎 0
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def isTree(root, subRoot) -> bool:
            if not subRoot and not root:
                return True
            if not subRoot or not root:
                return False
            if root.val != subRoot.val:
                return False
            return isTree(root.left, subRoot.left) and isTree(root.right, subRoot.right)

        return isTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# leetcode submit region end(Prohibit modification and deletion)
# [3,4,5,1,2]
# [4,1,2]

if __name__ == '__main__':
    print(Solution.isSubtree(None, [3, 4, 5, 1, 2], [4, 1, 2]))
