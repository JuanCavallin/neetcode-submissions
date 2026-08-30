class MedianFinder {
    private:
        priority_queue<int, vector<int>, greater<int>> minHeap;
        priority_queue<int> maxHeap;
    public:
        MedianFinder() {
            
        }
        
        void addNum(int num) {
            //push first to corresponding stack
            if(minHeap.size() == 0) {
                minHeap.push(num);
            }
            else if(num < minHeap.top()) {
                maxHeap.push(num);
            }
            else {
                minHeap.push(num);
            }

            //rebalance
            if(minHeap.size() > maxHeap.size() + 1) {
                int t = minHeap.top();
                minHeap.pop();
                maxHeap.push(t);
            }
        }
        
        double findMedian() {
            if(minHeap.size() == 0) {return 0;}
            if(maxHeap.size() == minHeap.size()) {
                return double(maxHeap.top() + minHeap.top()) / 2;
            }
            else {
                return minHeap.top();
            }
        }
    };
