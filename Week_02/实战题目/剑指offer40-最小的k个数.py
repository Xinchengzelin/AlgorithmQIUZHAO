class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        #直接用sort
        # arr.sort()
        # return arr[:k]

        #堆的思想-利用python的小顶堆
        if k==0:
            return []
        hp=[-x for x in arr[0:k]]
        heapq.heapify(hp)
        for i in range(k,len(arr)):
            if -arr[i] > hp[0]:
                heapq.heappop(hp)
                heapq.heappush(hp,-arr[i])
        ans=[-x for x in hp]
        return ans

        #快速排序