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
        if(head == nullptr) {return nullptr; }

        ListNode* prev = head;
        ListNode* after = head->next;
        while(after != nullptr) {
            //Swap
            ListNode* temp = after->next;
            if(prev == head) {
                prev->next = nullptr;
            }
            //Update pointers
            after->next = prev;
            prev = after;
            after = temp;
            
        }
        return prev; //head moved to new head

    }
};
