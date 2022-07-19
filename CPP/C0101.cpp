#include <iostream>
using namespace std;
struct TreeNode{
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() : val(0), left(nullptr), right(nullptr){} 
    TreeNode(int x) : val(x), left(nullptr), right(nullptr){} 
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right){}
                                                                                                                                                                                                   *
};
class Solution{
    public:
        bool isSymmetricRecursive(TreeNode *leftNode, TreeNode *rightNode){

            if (leftNode == NULL or rightNode == NULL){
                if (leftNode == rightNode)
                    return true;
                return false;
            }

            if (leftNode->val != rightNode->val){
                return false;
            }

            return isSymmetricRecursive(leftNode->left, rightNode->right) and isSymmetricRecursive(leftNode->right, rightNode->left);
        }

        bool isSymmetric(TreeNode *root){
            if (root == NULL)
                return true;
            return isSymmetricRecursive(root->left, root->right);
        }
};