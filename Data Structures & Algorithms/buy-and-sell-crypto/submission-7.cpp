#include <algorithm>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        //Buy low, sell high
        int max_profit = 0;
        int current_profit;
        int l = 0;
        int r = 1;
        
        //If r < l, update l and r
        //else, move r to the right and keep checking
        while(r < prices.size()) {
            current_profit = prices[r] - prices[l];
            if(current_profit > max_profit) {
                max_profit = current_profit;
                cout << "First: " << l << ", Last: " << r << endl;
            }
            if(prices[r] < prices[l]) {
                l++;
                if(l == r) {
                    r++;
                }
            }
            else {
                r++;
            }
        }
        
        return max_profit;
    }
};
