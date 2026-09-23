class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # gas[i] = amount of gas at that station
        # cost[i] = amount to go to i + 1 station

        # return the first index that I find that can travel in a clockwise
        # so if I start at 0 needs to just go around once plus the last
        # If I start at 2 need to go through end, then 0, 1, 2
        # I can probably do it in one loop if I can check whether each station can go to the next
        # maybe keep a visited set and a set for can reach the next. If next in 'linked' then add to linked and if size linked = length then return current idx
        # If size of visited = total in array then 


        # Take the amount of gas that you gain by travelling (gas[i] - cost[i]) then start at the largest point, 
        # What would be an edge case for this??? Feel like not just largest but need to start at  
        # Skip any negative values because can't start there 
        total = sum(gas) - sum(cost)
        if total < 0:
            return -1
        # Since larger this means that there has to be an index that can traverse so we check if possible and when we find where we can't we update by 1 since it has to be larger
        idx = 0
        current = 0
        for i in range(len(gas) - 1):
            current += gas[i] - cost[i]
            if current < 0:
                idx = i + 1
        return idx

