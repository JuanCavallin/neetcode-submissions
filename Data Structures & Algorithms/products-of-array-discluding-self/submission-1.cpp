using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        //Create vector and go through prefixes
        vector<int> result(nums.size());
        int block = 1; 
        result[0] = 1;
        //Prefixes
        for(int i = 1; i < nums.size(); i++) {
            block *= nums[i - 1];
            result[i] = block;
        }
        block = 1;
        //Postfixes
        for(int j = nums.size() - 2; j >= 0; j--) {
            block *= nums[j + 1];
            result[j] *= block;
        }

        return result;
    }
};
