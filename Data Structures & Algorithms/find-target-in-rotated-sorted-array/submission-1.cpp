class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;
        int m;
        while(l < r) {
            m = (l + r) / 2;
            cout << "Left: " << l << "Right: " << r << "Middle: " << m << endl;
            if(nums[m] == target) {
                return m;
            }
            if(nums[m] < nums[r]) {
                //Right side sorted
                //Check if target is in sorted side:
                if(target > nums[m] && target <= nums[r]) {
                    //Go right
                    l = m + 1;
                }
                else {
                    //Go left
                    r = m;
                }
            }
            else {
                //Left side sorted
                //Check if target is in sorted side: 
                if(target < nums[m] && target >= nums[l]) {
                    //Go left
                    r = m;
                }
                else {
                    //Go right
                    l = m + 1;
                }
            }
        }
        if(nums[l] == target) {
            return l;
        }
        else {
            return -1;
        }
    }
};
