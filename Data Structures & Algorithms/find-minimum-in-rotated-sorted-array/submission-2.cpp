class Solution {
public:
    int findMin(vector<int> &nums) {
        //Only solution I can think of: binary search but go to the side that is smaller
        //If mid < nums[r], then the num will be in the left 
        //If mid > nums[l], then left is the sorted part and it will be in the left
        int l = 0;
        int r = nums.size() - 1;
        int m = (l + r) / 2;
        while(l < r) {
            if(nums[m] < nums[r]) {
                r = m;
            }
            else {
                l = m + 1;
            }
            cout << "Left: " << l << ", Right: " << r << endl;
            m = (l + r) / 2;
        }
        return nums[l];
    }
};
