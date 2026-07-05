class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> set(begin(nums), end(nums));
        int max = 0;
        int current_seq = 1;
        for(int num : set) {
            int prev = num - 1;
            if(set.find(prev) == set.end()) { //Start of set
                int current = num + 1;
                while(set.find(current) != set.end()) {
                    cout << current << endl;
                    current += 1;
                    current_seq += 1;
                }
            if(current_seq > max) {
                max = current_seq;
            }
            current_seq = 1;
            }
        }
        return max;

    }
};