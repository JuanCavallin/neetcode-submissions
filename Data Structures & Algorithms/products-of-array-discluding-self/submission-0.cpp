class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int sum = 1;
        vector<int> products;
        bool contains_zero = false;
        bool contains_multiple_zeroes = false;
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] != 0)
                sum *= nums[i];
            else {
                if(contains_zero) {
                    contains_multiple_zeroes = true;
                    break;
                }
                contains_zero = true;
            }
        }

        if(contains_multiple_zeroes) {
            products = vector<int>(nums.size(), 0);

        }
        else if(contains_zero) {
            for(int n : nums) {
                if(n == 0)
                    products.push_back(sum);
                else 
                    products.push_back(0);
            }
        }
        else {
            for(int n : nums)
                products.push_back(sum / n);
        }
        return products;
    }
};
