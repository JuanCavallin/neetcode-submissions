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
    int kthSmallest(TreeNode* root, int k) {
        TreeNode* current = root;
        stack<TreeNode*> s; //For DFS
        int counter = 0; //Current nth lowest num
        //In-Order traversal, updating counter every time it is at lowest left val in current subtree
        while(s.size() > 0 || current != nullptr) {
            while(current != nullptr) {
                s.push(current);
                current = current->left;
            }
            current = s.top();
            s.pop();
            counter++;
            if(counter == k) {
                return current->val;
            }
            current = current->right;
        }
        return current->val;
    }
};
