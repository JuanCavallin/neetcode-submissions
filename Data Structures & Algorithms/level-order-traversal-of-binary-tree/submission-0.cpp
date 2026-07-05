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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if(root == nullptr) {
            return result;
        }
        // Perform BFS, need to use a queue
        queue<TreeNode*> q;
        TreeNode* current = root;
        q.push(current);
        while(q.size() != 0) {
            int s = q.size();
            vector<int> temp;
            for(int i = 0; i < s; i++) {
                current = q.front();
                //Add left and right to the queue
                if(current->left != nullptr) {
                    q.push(current->left);
                }
                if(current->right != nullptr) {
                    q.push(current->right);
                }
                
                //add current to the result vector (for this level) and pop
                temp.push_back(current->val);
                q.pop();
            }
            result.push_back(temp);

        }
        return result;
    }
};
