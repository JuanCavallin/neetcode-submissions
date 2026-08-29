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
//algorithm for comparing values in a lists of nodes, simplest and least overhead
        struct Compare {
            bool operator()(ListNode* a, ListNode* b) {
                return a->val > b->val; // > is for minHeap while < is for maxHeap
            }
        };
    ListNode* mergeKLists(vector<ListNode*>& lists) {

        priority_queue<ListNode*, vector<ListNode*>, Compare> minHeap; //Get the smallest from the k arrays to make into the next pointer

        ListNode dummy;
        ListNode* current = &(dummy);
        for(int i = 0; i < lists.size(); i++) {
            if(lists[i] != nullptr) {
                minHeap.push(lists[i]);
            }
                
            }
        while(minHeap.size() > 0) {

            ListNode* t = minHeap.top();
            current->next = t;
            minHeap.pop(); //remove the top node
            if(t->next != nullptr) {
                minHeap.push(t->next);
            }
            current = current->next;
        }
        return dummy.next;
    }
};
