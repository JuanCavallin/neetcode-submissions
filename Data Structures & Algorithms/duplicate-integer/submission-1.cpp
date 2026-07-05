using namespace std;
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        //Check if an array contains the same number twice
        //Algo: iterate through. Check if it contains the value or if not then add it
        unordered_set<int> n;
        for(int num : nums) {
            if(n.find(num) != n.end()) {
                return true;
            }
            else {
                n.insert(num);
            }
        }
        return false;
    }
};




