class MedianFinder {
public:
    priority_queue<int, std::vector<int>, std::greater<int>> minHeap; //top half
    priority_queue<int> maxHeap; //bottom half
    MedianFinder() {

    }
    
    void addNum(int num) {
        long maxSize = maxHeap.size();
        long minSize = minHeap.size();
        if(maxSize == 0 || num < maxHeap.top()) {
            maxHeap.push(num);
            maxSize++;
        }
        else {
            minHeap.push(num);
            minSize++;
        }
        
        //resize if needed
        if(minSize - 1 > maxSize) {
            //minHeap too large
            int k = minHeap.top(); minHeap.pop();
            maxHeap.push(k);
        }
        else if(maxSize - 1 > minSize) {
            int k = maxHeap.top(); maxHeap.pop();
            minHeap.push(k);
        }
    }
    
    double findMedian() {
        long maxSize = maxHeap.size();
        long minSize = minHeap.size();
        if(maxSize + minSize == 0) {
            return double(0);
        }
        if(maxSize > minSize) {
            return double(maxHeap.top());
        }
        else if(minSize > maxSize) {
            return double(minHeap.top());
        }
        else {
            //Both sizes equal, so even number
            double mean = double(minHeap.top() + maxHeap.top()) / 2;
            return mean;
        }
    }
};
