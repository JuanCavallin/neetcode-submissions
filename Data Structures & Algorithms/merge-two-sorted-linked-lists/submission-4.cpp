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
        if(list1 == nullptr) {
            return list2;
        }
        if(list2 == nullptr) {
            return list1;
        }
        
        //Set head pointer to return
        ListNode* head;
        if(list1->val < list2->val) {
            head = list1;
            list1 = list1->next;
        }
        else {
            head = list2;
            list2 = list2->next;
        }
        ListNode* current = head;

        while(list1 != nullptr && list2 != nullptr) {
            //Update list 1 or list 2 pointer and add to head->next
            ListNode* temp1 = list1->next;
            ListNode* temp2 = list2->next;

            //Swap next for whichever value is the smallest then 
            if(list1->val < list2->val) {
                current->next = list1;
                list1 = temp1;
            }
            else {
                current->next = list2;
                list2 = temp2;
            }
            current = current->next;
    }
    //Finish remainder of the list
    if(list1 != nullptr) {
        current->next = list1;
    }
    else {
        current ->next = list2;
    }

    return head;


        
    }
};
