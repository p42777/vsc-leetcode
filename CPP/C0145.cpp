#include <iostream>
using namespace std;

class TreeNode{
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val){
        this.val = val;
    }
    TreeNode(int val, TreeNode left, TreeNode right){
        this.val = val;
        this.left = left;
        this.right = right;
    }
};

class Solution{
    public:
        void helper(TreeNode *root, vector<int> &v){
            if (root == NULL)
                return;
            helper(root->left, v);
            helper(root->right, v);
            v.push_back(root->val);
        }
        vector<int> postorderTraversal(TreeNode *root)
        {
            vector<int> v;
            helper(root, v);
            return v;
        }
};
