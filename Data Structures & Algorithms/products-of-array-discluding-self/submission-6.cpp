class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        if(nums.size() == 1) {
            return vector<int>(nums[0]);
        }

        vector<int> left_prod(nums.size());
        vector<int> right_prod(nums.size());
        vector<int> result;
        int l = 1;
        int r = nums.size() - 2;
        left_prod[0] = 1;
        right_prod[nums.size() - 1] = 1;

        while(l < nums.size()) {
            left_prod[l] = left_prod[l - 1] * nums[l - 1];
            right_prod[r] = right_prod[r + 1] * nums[r + 1];
            //cout << "nums[l]: " << left_prod[l - 1] << "-----> ";
            //cout << left_prod[l] << ", " << right_prod[r] << endl;
            l++; 
            r--;
        }

        for(int i = 0; i < nums.size(); i++) {
            result.push_back(left_prod[i] * right_prod[i]);
        }
        return result;
    }
};
