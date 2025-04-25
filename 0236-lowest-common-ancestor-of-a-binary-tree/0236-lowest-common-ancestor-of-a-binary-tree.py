class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        check=[0]
        res=[None]
        def fun(root):
            nonlocal p,q
            if res[0]!=None:
                return False
            if root==None:
                return False 
            if (root==p or root==q) and check[0]==0 :
                check[0]=root
                left=fun(root.left)
                right=fun(root.right)
                if left or right:
                    res[0]=check[0]
                return True
            elif (root==p or root==q):
                return True
            else:
                left=fun(root.left)
                right=fun(root.right)
                if left and right:
                    res[0]=root
                    return True
                if left or right:
                    return True
                else:
                    return False
        fun(root)
        return res[0]