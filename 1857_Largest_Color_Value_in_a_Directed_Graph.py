


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
