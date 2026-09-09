class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        global_visited = set()
        order = [] 
        pre_map = {i:[] for i in range(numCourses) }

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        def dfs(course):
            # Same algorithm but need to keep track of the flow, I think just create an array and change the order at the end
            if course in visited:
                return False
            if pre_map[course] == []:
                return True
            if course not in global_visited:
                order.append(course)
            visited.add(course)
            global_visited.add(course)
            for pre in pre_map[course]:
                if not dfs(pre):
                    return False
            #Went through all the prereqs successfully
            pre_map[course] = [] #On future interations will not go through pre_reqs again 
            visited.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return order[::-1]
