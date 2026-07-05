class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int r = nums.size() - 1;
        int l = 0;
        vector<vector<int>> result;

        for(int k = 0; k < nums.size() - 2; k++) {
            //Elegant way to check for fastest case
            if(nums[k] > 0) break;

            //Check if duplicate k: Have to check previous instead of next because next may be included in the solution
            if(k > 0 && nums[k] == nums[k - 1]) { //Interesting note: does not give error due to k > 0 condition
                continue;
            }
            //Run 2 pointer solution
            l = k + 1;
            r = nums.size() - 1;
            while(l < r) {
                if(nums[l] + nums[r] + nums[k] == 0) {
                    vector<int> solution = {nums[k], nums[l], nums[r]};
                    result.push_back(vector<int>(solution));
                    //I MISSED AN IMPORTANT STEP HERE. There may be more than one answer with this first pointer value, so continue:
                    //Before, this was doing an infinite loop
                    r--; l++;
                    while (l < r && nums[l] == nums[l - 1]) { //Avoid duplicate solutions with same l
                        l++;
                    }

                }
                else if(nums[l] + nums[r] + nums[k] > 0) {
                    r--;
                }
                else {
                    l++;
                }
            }
        }
        return result;
        
    }
};
