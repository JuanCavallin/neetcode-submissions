#include <iostream>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        //Return the k most frequent elements in nums
        //Have a hash map with each num as the key and the value as its frequency
        //What unique about this problem: use bucket sort
        /** 
        1. Use an object that has the count as an index and the value as the list of nums that appear
        2. Traverse backwards until k are found and are popped. 
        */
        unordered_map<int, int> num_frequency;
        vector<vector<int>> frequency_nums(nums.size() + 1);
        vector<int> result;
        int count = 0;
        for(int num : nums) {
            num_frequency[num]++;
        } 
        for(const auto& pair : num_frequency) {
            frequency_nums[pair.second].push_back(pair.first);
            //cout << frequency_nums[pair.second] << endl;
        }

        for(int i = frequency_nums.size() - 1; i > 0; i--) {
            for(const int& n : frequency_nums[i]) {
                if(count < k) {
                    result.push_back(n);
                    count++;
                }
                else {
                    return result;
                }
            }
        }
        return result;
    }
};
