# 1441. Build an Array With Stack Operations.py

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        output = []
        s = set(target) # Improves Look Up Performance
        
        for i in range(1,target[-1]+1): # Checks Last Element of Array to Stop Early
            output.append("Push")
            if i not in s:
                output.append("Pop")
        return output
        
