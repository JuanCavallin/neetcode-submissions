class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> num_to_frequency;
        vector<vector<int>> counts(nums.size() + 1);
        vector<int> result;

        for(int i = 0; i < nums.size(); i++) {
            num_to_frequency[nums[i]]++;
        }
        for(const auto& pair : num_to_frequency) {
            counts[pair.second].push_back(pair.first);
        }

        for(int i = counts.size() - 1; i > 0; i--) {
            for(int n : counts[i]) {
                if(result.size() < k) {
                    result.push_back(n);
                }
                else {
                    return result;
                }
            }
        }

    return result;
    }
};
