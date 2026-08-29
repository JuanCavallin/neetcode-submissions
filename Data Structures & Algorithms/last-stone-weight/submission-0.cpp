class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> maxHeap;
        //Insert values from the stones, may be faster way to write
        for(int i = 0; i < stones.size(); i++) {
            maxHeap.push(stones[i]);
        }

        // Pop the two top, then insert 1 - 2
        while(maxHeap.size() > 1) {
            int a = maxHeap.top();
            maxHeap.pop();
            int b = maxHeap.top();
            maxHeap.pop();
            maxHeap.push(a - b);
        }
        return maxHeap.top();
    }
};
