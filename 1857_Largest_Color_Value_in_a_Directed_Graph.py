'''
There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed).
You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.
'''
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n=len(colors)
        adj=[[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
        
        visited=[0]*n
        tp=[]
        cycle=False

        def dfs(node):
            nonlocal cycle
            if visited[node]:
                if visited[node]==1:
                    cycle=True
                return
            visited[node]=1
            for c in adj[node]:
                dfs(c)
            visited[node]=2
            tp.append(node)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                
        if cycle:
            return -1
        tp.reverse()
        
        colors=[ord(c)-ord('a') for c in colors]
        ans=0
        for c in range(26):
            dp=[0]*n
            for v in tp:
                if colors[v]==c:
                    dp[v]+=1
                    ans=max(ans,dp[v])
                for k in adj[v]:
                    dp[k]=max(dp[k],dp[v])
        return ans
    
   
