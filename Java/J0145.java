package Java;
import java.util.ArrayList;
import java.util.List;

public class J0145 {
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }
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
        public List<Integer> postorderTraversal(TreeNode root) {
            List<Integer> result = new ArrayList<>();
            depthFirstSearch(root, result);
            return result;

        }

        public void depthFirstSearch(TreeNode root, List<Integer> result) {
            if (root == null)
                return;
            depthFirstSearch(root.left, result);
            depthFirstSearch(root.right, result);
            result.add(root.val);

        }
    }
}
