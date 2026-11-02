class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for a, b in prerequisites:
            graph[a].add(b)
        
        
        # need to take b before a
        # Turn into graph where b has all of this edges, then traverse. If there are any loops then return False, or if all of the visited courses matches numCourses (pretty sure that is another condition I need to verify)
        # Also need to check starting will all of the courses not just 1, so keep visited. 
        # ?? Do I need to track the current path????

        # if I do a --> b, then every time I fill a prereq I can 
        def bfs(root):
            queue = deque([root])
            path = set([root])
            #path.add(root)
            while queue:
                current = queue.popleft()
                path.add(current)
                #print("Current:", current)
                for neighbor in graph[current]:
                    #print("Neighbor:", neighbor)
                    if neighbor in path:
                        return False
                    queue.append(neighbor)
                    #path.add(neighbor)
                # Since we visited every neighbor, we can just remove all of them at once after
                graph[current] = set()

            return True

        for i in range(numCourses):
            if not bfs(i):
                return False
        return True


