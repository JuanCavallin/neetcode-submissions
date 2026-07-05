#include <string>
#include <cctype>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.length() - 1;

        while (l < r) {
            // Move l to the next alphanumeric character
            while (l < r && !isalnum(s[l])) {
                l++;
            }

            // Move r to the previous alphanumeric character
            while (l < r && !isalnum(s[r])) {
                r--;
            }

            // Compare characters (case-insensitive)
            if (tolower(s[l]) != tolower(s[r])) {
                return false;
            }

            l++;
            r--;
        }

        return true;
    }
};
