class Solution {
public:
    int hammingWeight(uint32_t n) {
        //Since integer is 32-bit, we iterate 32 times. This makes it O(1) instead of O(n) (useful hack)
        int count = 0;
        for(int i = 0; i < 32; i++) {
            //Need to use a bitwise operator to get whether 1 or 0
            if(n % 2 == 1) {
                count++;
            }
            n = n >> 1;
        }
        return count;
    }
};
