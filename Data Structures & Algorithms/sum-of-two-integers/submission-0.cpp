class Solution {
public:
    int getSum(int a, int b) {
        //Go through each bit, use XOR operation, do XOR again with carry, calculate new carry
        int result = 0;
        int carry = 0;
        for(int i = 0; i < 32; i++) {
            int abit = a & 1;
            int bbit = b & 1;
            int temp = abit^bbit;
            result |= ((temp^carry) << i);
            cout << "Temp: " << temp << endl;
            cout << "Current result: " << result << endl;

            //Calculate carry
            //Needs to take into account if any bit == 1 + the previous carry = 1
            if(abit & bbit || abit & carry | bbit & carry) {
                carry = 1;
            }
            else {
                carry = 0;
            }
            //Shift a and b to compute next digit
            a = a >> 1;
            b = b >>= 1;
        }
        return result;
    }
};
