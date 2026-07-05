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
    void reorderList(ListNode* head) {
        //Reorder the second half of the list and merge first half[i] with second half[i]
        ListNode* second = head;
        ListNode* first = head;
        ListNode* fast = head;
        //int second_idx = 0;
        while(fast != nullptr && fast->next != nullptr) {
            second = second->next;
            fast = fast->next->next;
            //second_idx++;
        }
        //cout << "Second: " << second->val << endl;
        ListNode* prev = nullptr;
        ListNode* mid = second;
        second = second->next;
        mid->next = nullptr;
        //second = second->next;
        while(second != nullptr) {
            ListNode* temp = second->next;
            second->next = prev;
            prev = second;
            second = temp;
        }
        second = prev;

        while(second != nullptr) {
            ListNode* temp1 = first->next;
            ListNode* temp2 = second->next;
            first->next = second;
            second->next = temp1;
            first = temp1;
            second = temp2;
        }
        
    }
};
