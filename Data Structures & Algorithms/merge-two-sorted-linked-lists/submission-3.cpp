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
        //Iterate until one pointer reaches the end, or add the next one if one of them equal nullptr
        ListNode head;
        ListNode* current = &head;
        while(list1 != nullptr || list2 != nullptr) {
            //Update list 1 or list 2 pointer and add to head->next
            if(list1 == nullptr) {
                current->next = new ListNode(list2->val);
                list2 = list2->next;

            } 
            else if(list2 == nullptr) {
                current->next = new ListNode(list1->val);
                list1 = list1->next;
            }
            else {
                //add the smallest of the two
                if(list1->val < list2->val) {
                    current->next = new ListNode(list1->val);
                    list1 = list1->next;
                }
                else {
                    current->next = new ListNode(list2->val);
                    list2 = list2->next;
                }
            }

            //Update head pointer
            current = current->next;
        }
        return head.next;


        
    }
};
