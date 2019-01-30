class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if(len(s) < numRows or numRows == 1):
            return s
        res = [''] * numRows
        index = 0
        direction = 1
        for i in s:
            res[index] += i
            if index == 0:
                direction = 1
            elif index == numRows - 1:
                direction = -1
            index += direction

        return ''.join(res)  
            
if __name__ == "__main__":
    solution = Solution()
    assert solution.convert("PAYPALISHIRING", 4) == 'PINALSIGYAHRPI'