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
        if(head == nullptr) {
            return nullptr;
        }
        ListNode* prev = head;
        ListNode* current = prev->next; // does this stay constant after next fix? I think so
        prev->next = nullptr;
        ListNode* next_node;
        while(current != nullptr) {
            next_node = current->next;
            //Set pointer for current to previous
            current->next = prev;
            //Adjust prev and current pointers: prev set to current, current set to next_node
            prev = current;
            current = next_node;
        }
        return prev;
    }
};
