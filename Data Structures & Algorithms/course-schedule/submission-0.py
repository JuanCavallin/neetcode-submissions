class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = { i:[] for i in range(numCourses)}
        visited = set()

        #populate the map
        for course, pre in prerequisites:
            pre_map[course].append(pre)

        #Implement dfs solution
        def dfs(course): 
            if course in visited:
                return False
           
            if pre_map[course] == []:
                return True
            
            visited.add(course)
            for pre in pre_map[course]:
                if not dfs(pre):
                    return False
            visited.remove(course) # After finishing recursive path and backtracking remove
            pre_map[course] = []
            return True
        
        #Need to loop in case the graph is not fully connected
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True




        