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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        //Duplicate merge logic for 2 lists, once done adjust one of the pointers to be the next in the array and continue for the rest of the array
        ListNode dummy;
        for(int i = 1; i < lists.size(); i++) {
            ListNode* a = lists[i - 1];
            ListNode* b = lists[i];
            ListNode* current = &dummy;
            while(b != nullptr && a != nullptr) {
                if(a->val < b->val) {
                    current->next = a;
                    a = a->next;
                }
                else {
                    current->next = b;
                    b = b->next;
                }
                //Adjust all pointers forward
                current = current->next;
            }
            current->next = (a != nullptr) ? a : b;

        }

        return dummy.next;
        
    }
};
