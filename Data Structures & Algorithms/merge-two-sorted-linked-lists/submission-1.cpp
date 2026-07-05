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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* curr1 = list1; //head
        ListNode* curr2 = list2;
        if(curr2 == nullptr) { return curr1; }
        if(curr1 == nullptr) { return curr2; }
        ListNode* ret = nullptr;
        ListNode* curr_ret = ret; 
        while(curr1 != nullptr || curr2 != nullptr) {
            if(curr2 == nullptr || (curr1 != nullptr && curr1->val <= curr2->val)) {
                if(ret == nullptr) { 
                    ret = curr1; 
                    curr_ret = ret;
                    }
                else {
                    curr_ret->next = curr1;
                    curr_ret = curr_ret->next;

                }
                curr1 = curr1->next;
            }
            else {
                if(ret == nullptr) { 
                    ret = curr2; 
                    curr_ret = ret;
                }
                else {
                    curr_ret->next = curr2;
                    curr_ret = curr_ret->next;
                }
                curr2 = curr2->next;
            }
        }
        return ret;
    }
};
