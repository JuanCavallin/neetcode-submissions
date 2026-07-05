#include <algorithm>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.length() <= 1) {
            return s.length();
        }


        int l = 0; int r = 1;
        unordered_set<int> set; 
        int max_count = 0;
        set.insert(s[l]);
        while(r < s.length()) {
        if(set.find(s[r]) == set.end()) {
            set.insert(s[r]);
            cout << "Inserted. l: " << l << ", r: " << r << endl;
        }
        else {
            if(set.size() > max_count) {
                max_count = set.size();
            }
            while(set.find(s[r]) != set.end()) {
                set.erase(s[l]);
                l++;
            }
            set.insert(s[r]);
        }
            r++;
        }

        if(max_count > set.size()) {
            return max_count;
        }
        return set.size();
    }
};
