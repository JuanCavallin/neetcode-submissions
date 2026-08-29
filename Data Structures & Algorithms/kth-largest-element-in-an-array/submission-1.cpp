class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int s = nums.size();
        int target = s - k;
        auto quickSelect = [&](auto&& self, int l, int r) -> int {
            int pivot = nums[r]; //use rightmost as the pivot, can be any
            int p = l;
            for(int i = l; i < r; i++) {
                //Swapping logic: if less than the pivot swap with the current partition value and increment that further, now the p index tells you how many values are smaller than the pivot and lets you adjust halves
                if(nums[i] < pivot) {
                    int temp = nums[i];
                    nums[i] = nums[p];
                    nums[p] = temp;
                    p += 1;
                }
            }
            //Swap pivot with p
            swap(nums[p], nums[r]);
            //Return if found if not then continue iteratively with the correct half
            if(p < target) {
                return self(self, p + 1, r);
            }
            else if (p > target) {
                return self(self, l, p - 1);
            }
            else {
                return nums[p];
            }
        };
        return quickSelect(quickSelect, 0, s - 1);
    }
};
