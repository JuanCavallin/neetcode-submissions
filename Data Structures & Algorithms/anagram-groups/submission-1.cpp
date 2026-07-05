using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        //Make a hash map that uses a key for each matching and and values with the origninal strings
        //Return a 2d vector string. Push a vector containing each of the strings at each key
        unordered_map<string, vector<string>> map;
        //Iterate through each string. Generate the int array[] with the count of each char. 
        //Create a string and push each count into that string
        for(const auto& str : strs) {
            vector<int> chars(26, 0);
            for(char c : str) {
                chars[c - 'a']++;
            }
            string key = to_string(chars[0]);
            for(int i = 1; i < chars.size(); i++) {
                key += ',' + to_string(chars[i]);
            }
            map[key].push_back(str);
        }
        //Return 2d vector
        vector<vector<string>> result;
        for(const auto& pair : map) {
            result.push_back(pair.second);
        }
    return result;
    }
};

