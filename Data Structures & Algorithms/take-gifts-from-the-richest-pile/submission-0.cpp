class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        //might want to make into a pair that holds the index to modify the original values to save a copy operation
        priority_queue<pair<int, int>> pq;
        //populate
        for(int i = 0; i < gifts.size(); i++) {
            pq.push(pair<int,int>{gifts[i], i});
        }
        for(int i = 0; i < k; i++) {
            auto t = pq.top();
            t.first = sqrt(t.first);
            cout << "Original: " << gifts[t.second] << "Now: " << t.first << endl;
            gifts[t.second] = t.first;
            pq.pop();
            pq.push(t);
        }
        long long sum = 0;
        for(int n : gifts) {
            sum += n;
        }
        return sum;
    }
};