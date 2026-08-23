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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* slow = head;
        ListNode* fast = head;
        for(int i = 0; i < n; i++) {
            fast = fast->next;
        }
        // This is what I missed. If fast == nullptr, then we are removing the head, actually easier. 
        if(fast == nullptr) {
            return head->next;
        }

        while(fast->next != nullptr) {
            fast = fast->next;
            slow = slow->next;
        }
        //Swap
        slow->next = slow->next->next;
        return head;
    }
};
