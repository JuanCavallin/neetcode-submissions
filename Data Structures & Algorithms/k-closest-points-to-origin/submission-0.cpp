class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        //double eucledian(vector<int>& a, vector<int>& b) {
        //    return math.sqrt(a[0] - b[0] ** 2 + (a[1] - b[1]) ** 2);
        //}

        struct Compare {
            bool operator()(vector<int>& a, vector<int>& b) {
                return sqrt(pow(2, a[0]) + pow(2,a[1])) > sqrt(pow(2, b[0]) + pow(2,b[1]));
            }
        };

        vector<vector<int>> result;
        priority_queue<vector<int>, vector<vector<int>>, Compare> minHeap;
        //Push all the points
        for(vector<int>& v : points ) {
            minHeap.push(v);
        }
        //Pop k elements and add to result
        for(int i = 0; i < k; i++) {
            result.push_back(minHeap.top());
            minHeap.pop();
        }
        return result;

        //TODO: later version where we compare and get the points with the largest distances from each other
    }
};
