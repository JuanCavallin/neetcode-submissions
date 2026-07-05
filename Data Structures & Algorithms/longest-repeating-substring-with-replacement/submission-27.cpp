class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> m(26);
        int max = 0;
        int l = 0; int r = 0; int window;
        int max_char = 0;
        while(r < s.length()) {
            char c = s[r];
            m[c]++;
            max_char = std::max(max_char, m[c]);
            if(r - l + 1 > k + max_char) {
                m[s[l]]--;
                l++;
            }
            max = std::max(max, r - l + 1);
            r++;
        }
        return max;

    }
};
