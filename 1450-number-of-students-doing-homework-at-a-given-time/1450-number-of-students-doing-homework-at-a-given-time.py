class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans=0
        
        for i in range(len(startTime)):
            if startTime[i]<=queryTime and endTime[i]>=queryTime:
                ans+=1
                
        return ans