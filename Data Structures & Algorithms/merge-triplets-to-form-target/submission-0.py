class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        current = [0, 0, 0]
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                a = max(triplet[0], current[0])
                b = max(triplet[1], current[1])
                c = max(triplet[2], current[2])
                current = [a, b, c]
        
        return current == target
        