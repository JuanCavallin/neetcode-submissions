class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        # graph generation is the hardest part for this problem
        result = []
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                temp = word[0:i] + "*" + word[i + 1:]
                graph[temp].append(word)
        
        visited = {} # node --> length
        # There is a condition that if we 
        parents = defaultdict(list) # node --> all previous, so once I find I have to run dfs through this graph to insert all of the paths that were found, unless there is a simplification


        # TODO: check if there is a way to simplify the graph
        # Run BFS so that I can keep track of all of the shortest paths, need to track visited with length of the sequence as well

        # Now I am starting to get the difference between this and Djikstras. In this we only check if it is equal and append to the parents array else skip. In djikstras we still have to compare using weights to see if it is less or more
        queue = deque()
        queue.append((beginWord, 0))
        visited[beginWord] = 0

        # start from endWord, iterate through parents array and fill everything into result

        while queue:
            current, dist = queue.popleft() # If I was keeping track of the length I might have to add that to the queue as well but double check
            if current == endWord:
                break
            for i in range(len(current)):
                temp = current[0:i] + "*" + current[i + 1:]
                for neighbor in graph[temp]:
                    if neighbor in visited:
                        if visited[neighbor] == dist + 1: 
                            parents[neighbor].append(current)
                        continue
                    parents[neighbor].append(current)
                    visited[neighbor] = (dist + 1)
                    queue.append((neighbor, dist + 1))

        if endWord not in visited:
            return []

        path = [None] * (visited[endWord] + 1)

        def dfs(current, idx):
            path[idx] = current

            if current == beginWord:
                result.append(path.copy())
                return

            for parent in parents[current]:
                dfs(parent, idx - 1)

        dfs(endWord, len(path) - 1)

        return result # empty list



        
