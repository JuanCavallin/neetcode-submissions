#include <iostream>
#include <algorithm>
using namespace std; 

class Solution {
public:
    int maxArea(vector<int>& heights) {
        int first = 0; int last = heights.size() - 1;
        int width = 0; 
        int max_height = max(heights[first], heights[last]);
        int current_height = min(heights[first], heights[last]); 
        int max_area = last * current_height; 
        int current_area = 0;
        while(first < last) {
            if(heights[first] < max_height) {
                //Increment first. Update max_area. 
                //max_height = heights[first];
                first++;
            }
            else {
                //Decrement last and update max area. 
                //max_height = heights[first];
                last--;

            }
            max_height = max(heights[first], heights[last]);
            current_height = min(heights[first], heights[last]); 
            current_area = (last - first) * current_height;
            if(max_area < current_area) {
                max_area = current_area;
            }
        }
    return max_area; 
    }
};
