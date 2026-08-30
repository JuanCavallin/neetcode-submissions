class MedianFinder {
    private:
        priority_queue<int, vector<int>, greater<int>> minHeap;
        priority_queue<int> maxHeap;
    public:
        MedianFinder() {
            
        }
        
        void addNum(int num) {
            minHeap.push(num);
            if(minHeap.size() > maxHeap.size()) {
                int t = minHeap.top();
                minHeap.pop();
                maxHeap.push(t);
            }
            else {
                //equal sizes, do nothing
            }
        }
        
        double findMedian() {
            if(maxHeap.size() == 0) {return 0;}
            if(maxHeap.size() == minHeap.size()) {
                return double(maxHeap.top() + minHeap.top()) / 2;
            }
            else {
                return maxHeap.top();
            }
        }
    };
