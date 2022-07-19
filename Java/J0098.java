package Java;
public class J0098 {
    
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) {
            this.val = val;
        }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    class Solution {
        public boolean isValidBST(TreeNode root) {
            if (root == null){
                return true;
            }
            return depthFirstSearch(root, null, null);
        }
        private boolean depthFirstSearch(TreeNode root, Integer min, Integer max) {
            if (root == null){
                return true;
            }
            if ((min != null && root.val <= min) || max != null && root.val >= max) {
                return false;
            }
            return depthFirstSearch(root.left, min, root.val) && depthFirstSearch(root.right, root.val, max);
        }
    }

}
