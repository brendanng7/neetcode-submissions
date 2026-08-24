class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # make adj list
        adj = [[] for _ in range(n)]
        for time in times:
            ui, vi, ti = time
            adj[ui-1].append((vi-1, ti))
        
        dist = [math.inf] * n
        dist[k-1] = 0
        minHeap = [(0, k-1)]
        heapq.heapify(minHeap)

        while minHeap:
            currDist, srcNode = heapq.heappop(minHeap)
            if currDist > dist[srcNode]:
                continue
            for edge in adj[srcNode]:
                destNode, timeTaken = edge
                if currDist + timeTaken < dist[destNode]:
                    dist[destNode] = dist[srcNode] + timeTaken
                    heapq.heappush(minHeap, (dist[destNode], destNode))

        res = max(dist)
        return res if res != math.inf else -1