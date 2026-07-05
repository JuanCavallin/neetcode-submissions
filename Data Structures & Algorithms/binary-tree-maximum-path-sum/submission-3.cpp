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
    int dfs(TreeNode* root, int& global_max) {
    //Do dfs
        if(root == nullptr) {
            return 0;
        }
        int left_sum = max(dfs(root->left, global_max), 0);
        int right_sum = max(dfs(root->right, global_max), 0);

        int current_max = root->val + left_sum + right_sum;
        //if(root->val > 0) path_max += root->val;
        global_max = max(global_max, current_max);
        return root->val + max(left_sum, right_sum);
    }
public:
    int maxPathSum(TreeNode* root) {
        int result = root->val;
        dfs(root, result);
        return result;
    }
};
