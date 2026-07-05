class Solution {
public:
    vector<int> countBits(int n) {
        int offset = 1;
        vector<int> result;
        result.push_back(0);
        for(int i = 1; i <= n; i++) {
            if(i == offset * 2) {
                offset *= 2;
            }
            int k = 1 + result[i - offset];
            result.push_back(k);
        }
        return result;
    }
};
