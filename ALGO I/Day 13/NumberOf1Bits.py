class Solution:
    def hammingWeight(self, n: int) -> int:
#         y=str(n)
#         x=list(map(int,y.strip()))
#         return (x.count(1))
        
          return bin(n).count('1')
