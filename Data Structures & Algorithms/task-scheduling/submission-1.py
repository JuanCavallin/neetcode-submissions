from collections import defaultdict
import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = defaultdict(int)
        for task in tasks:
            frequencies[task] += 1
        pq = []
        #max heap = min heap but multiply values by -1

        for key, val in frequencies.items():
            heapq.heappush(pq, [val * -1, key])
        k = 0
        result = 0
        queue = deque()
        while pq or queue:
            if k == n + 1:
                k = 0
                while queue:
                    top = queue.popleft()
                    heapq.heappush(pq, top)
            if pq:
                top = heapq.heappop(pq)
                top[0] += 1
                if top[0] != 0:
                    queue.append(top)
            result += 1
            k += 1
        return result

