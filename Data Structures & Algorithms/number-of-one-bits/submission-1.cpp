class Solution {
public:
    int hammingWeight(uint32_t n) {
        //Since integer is 32-bit, we iterate 32 times. This makes it O(1) instead of O(n) (useful hack)
        int count = 0;
        //Fastest check: remove every 1 bit at each step so that you only iterate through the number of 1s
        while(n > 0) {
            n &= n - 1;
            count++;
        }
        /*
        for(int i = 0; i < 32; i++) {
            //Need to use a bitwise operator to get whether 1 or 0
            //if n & 1 == 1 --> does AND with number and 00000001, returning 0 for all places and 1 for the last one
            if(n % 2 == 1) { 
                count++;
            }
            n = n >> 1; 
        }
        */
        return count;
    }
};
