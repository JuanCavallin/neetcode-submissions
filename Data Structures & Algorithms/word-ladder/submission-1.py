class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()
        graph = defaultdict(list)
        if wordList == []:
            return 0
        if len(wordList[0]) == 1:
            return 1
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
                

        #Run DFS from the starting word
        count = 0
        def dfs(word, prev):
            nonlocal count
            if word in visited:
                return False
            if word == endWord:
                count += 1
                return True
            visited.add(word)
            for neighbor in graph[word]:
                if neighbor == prev:
                    continue
                if(dfs(neighbor, word)):
                    if '*' not in word:
                        count += 1
                    return True
            return False
        
        dfs(beginWord, '')
        return count


