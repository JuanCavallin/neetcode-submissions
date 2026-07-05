class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int result = 0;
        for(int i = 0; i < 32; i++) {
            //Get bit at bottom position and add 
            int bit = n & 1;
            result |= (bit << (31 - i));
            n = n >> 1;
        }
        return result;
    }
};
