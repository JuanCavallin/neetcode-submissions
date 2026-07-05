//Two solutions:
//1. Make two hash tables and see if they are equal
//2. Use a hash table. Subtract one at the index of each char in a string and add one at each index equal to a char in the other string.  
// - If they are equal, the value at each index should equal zero 

class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size())
            return false;

        unordered_map<int, int> str_values;
        for(int i = 0; i < s.size(); i++) {
            str_values[s[i] - 'a']++; //the minus 'a' converts the char into a int equal to the position in the alphabet (0 indexed)
            str_values[t[i] - 'a']--;
        }

        for(int j = 0; j < s.size(); j++) {
            if(str_values[s[j] - 'a'] != 0)
                return false;
        }
        return true;
    }
};
