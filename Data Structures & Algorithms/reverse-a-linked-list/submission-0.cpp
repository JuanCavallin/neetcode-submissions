/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* current = head;
        while(current != nullptr) {
            ListNode* temp = current->next;
            //cout << "Temp: " << temp->val << endl;
            current->next = prev;
            prev = current;
            current = temp;
            //cout << "Temp: " << temp->val << endl;
        }
        return prev;
    }
};
