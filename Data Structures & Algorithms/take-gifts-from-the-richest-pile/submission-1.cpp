class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        priority_queue<int> pq(gifts.begin(), gifts.end());
        for(int i = 0; i < k; i++) {
            auto t = pq.top();
            t = sqrt(t);
            pq.pop();
            pq.push(t);
        }
        long long sum = 0;
        while(pq.size() > 0) {
            sum += pq.top();
            pq.pop();
        }
        return sum;
    }
};