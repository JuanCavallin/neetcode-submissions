class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        //Fastest and simplest: sort and return nums[k] - O(n log (n))

        //No sorting: use maxHeap
        priority_queue<int> maxHeap(nums.begin(), nums.end());
        for(int i = 0; i < k -1; i++) {
            maxHeap.pop();
        }
        return maxHeap.top();
        
    }
};
