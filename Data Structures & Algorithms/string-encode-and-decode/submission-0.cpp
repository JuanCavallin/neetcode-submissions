class Solution {
public:

    string encode(vector<string>& strs) {
        string result = "";
        for(string s : strs) {
            result = result + s + "_____";
        }
        return result;
    }

    vector<string> decode(string s) {
        vector<string> result;
        while(s.length() > 0) {
            int idx = s.find("_____");
            string segment = s.substr(0, idx);
            result.push_back(segment);
            s = s.substr(idx + 5);
        }
        return result;
    }
};
