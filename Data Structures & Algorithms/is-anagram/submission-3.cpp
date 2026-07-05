class Solution {
public:
    bool isAnagram(string s, string t) {
        //Check if two strings are anagrams of each other
        //Make a hash table of key: char and value: number of time it appears
        //Iterate through s and add 1 for each element
        //Iterate through t and subtract 1 for each element
        //If finds value > 0: return false. Else, return true
        if(s.size() != t.size())
            return false;

        unordered_map<char, int> table;
        for(int i = 0; i < s.size(); i++) { //does not take into account duplicates
            table[s[i]]++;
            table[t[i]]--;
        }
        for(auto c: table) {
            if(c.second != 0)
                return false;
        }
        return true;



        
        if(s.size() != t.size())
            return false;
        unordered_set<char> s_set;
        unordered_set<char> t_set;
        for(int i = 0; i < s.size(); i++) { //does not take into account duplicates
            s_set.insert(s[i]);
            t_set.insert(t[i]);
        }
        if(s_set == t_set) {
            return true;
        }
        else {
            return false;
        }
    }
};
