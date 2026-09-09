class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if wordList == []:
            return 0
        visited = set()
        graph = defaultdict(list)

        #Create the graph
        for i in range(len(wordList)):
            word = wordList[i]
            for j in range(len(word)):
                parent = word[:j] + '*' + word[j + 1:]
                graph[parent].append(word)
                graph[word].append(parent)
                if parent == beginWord[:j] + '*' + beginWord[j + 1:]:
                    graph[parent].append(beginWord)
                    graph[beginWord].append(parent)
                

        #Run BFS from the starting word
        queue = deque([(beginWord, 1)])
        visited.add(beginWord)
        while queue:
            current, length = queue.popleft()
            if current == endWord:
                return length

            for i in range(len(current)):
                pattern = current[:i] + '*' + current[i + 1:]

                for neighbor in graph[pattern]:
                    if neighbor not in visited:
                        queue.append((neighbor, length + 1))
                        visited.add(neighbor)

        return 0


