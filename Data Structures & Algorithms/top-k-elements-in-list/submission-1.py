class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        #Make array with counts
        for num in nums:
            #d[num]++ Works in C++
            d[num] = d.get(num, 0) + 1 #add 1 to the value 
        
        #Sort array and take out the top k elements
        count_to_num =  []
        for num, count in d.items():
            count_to_num.append([count, num])
        count_to_num.sort(reverse = True)

        #Add the values into return array
        result = []
        for i in range(k): 
            result.append(count_to_num[i][1])
        return result