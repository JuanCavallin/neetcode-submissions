#include <limits>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool helper(TreeNode* root, long long lowest, long long highest) {
        if(root == nullptr) {
            return true;
        }
        //check current node
        if(root->val >= highest || root->val <= lowest) {
            return false;
        }
        return(helper(root->left, lowest, root->val) && helper(root->right, root->val, highest));
    }

    bool isValidBST(TreeNode* root) {
        if(root == nullptr) {
            return true;
        }
        return helper(root, numeric_limits<long long>::min(), numeric_limits<long long>::max());
    }
};
