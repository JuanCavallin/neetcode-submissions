class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        //Iterate through vector and find two nums that add up to target
        //Make a hash set of numbers
        //For every num in nums, check if target - num is in the hash set

        //unordered_set<int> converse(nums.begin(), nums.end());
        unordered_map<int, int> converse;
        
        for(int i = 0; i < nums.size(); i++) {
            int opposite = target - nums[i]; 
            if(converse.find(opposite) != converse.end()) {
                return {converse[opposite], i};
            }
            converse.insert({nums[i], i});
        }
        return {};
    }
};
