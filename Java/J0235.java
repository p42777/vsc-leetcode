package Java;

public class J0235 {

    public class TreeNode {

        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    class Solution {

        public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {

            if (p.val > root.val && q.val > root.val) // both in right subtree
                return lowestCommonAncestor(root.right, p, q);
            if (p.val < root.val && q.val < root.val) // both in left subtree
                return lowestCommonAncestor(root.left, p, q);
            // if one in left subtree and one in right subtree return root
            return root; 
        }
    }

}
