#:encoding:utf-8
"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI" 34 46 58
Explanation:

P     I    N
A   L S  I G  
Y A   H R
P     I

P [0][0]
A [1][0]
Y [2][0]
P [3][0]

A [2][1]
L [1][2]

I [0][3]
S [1][3]
H [2][3]
I [3][3]

R [2][4]
I [1][5]

N [0][6]

"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = []
        s_len = len(s)
        period_items = (numRows-1)*2  # 一个周期所包含的元素个数
        times = s_len // period_items  # 有几个完整周期
        max_line_len = (times+1)*(numRows-1) # 每一行可能的最大长度
        for i in range(numRows):
            line_list = []
            for i in range(max_line_len):
                line_list.append('')
            res.append(line_list)
        # print res

        jj_index = 0 # 表示第几个周期的第一个元素的列下标
        cnt = 0
        inclide_c = 1
        # 往res列表填写数
        while cnt<s_len:
            c = cnt%period_items
            if 0<cnt%period_items <numRows:
                res[cnt%period_items][jj_index] = s[cnt]
                cnt += 1
            elif numRows<=cnt%period_items <period_items:
                colume1111 = jj_index + inclide_c
                line111111 = jj_index + numRows - 1 - (jj_index + inclide_c)
                res[line111111][colume1111] = s[cnt]
                inclide_c += 1
                cnt +=1
            else:
                if cnt >1:
                    jj_index +=  numRows - 1
                res[0][jj_index] = s[cnt]
                cnt += 1
                inclide_c = 1
        s = ''       
        for i in res:
            s+=''.join(i)
        return s
if __name__ == "__main__":
    solution = Solution()
    assert solution.convert("PAYPALISHIRING", 4) == 'PINALSIGYAHRPI'
    assert solution.convert("PAYPALISHIRING", 3) == 'PAHNAPLSIIGYIR'
