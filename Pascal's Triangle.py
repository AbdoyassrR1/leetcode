#!/usr/bin/python3

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        triangle = []
        pre = 0
        next = pre + 1
        triangle.append([pre + next])
        for i in range(numRows - 1):
            pre = 0
            next = pre + 1
            new_row = []
            new_row.append(1)
            for num in range(len(triangle[i])):
                if next > len(triangle[i]) - 1 or pre == len(triangle[i]) - 1:
                    # new_row.append(triangle[0][pre] + 0)
                    new_row.append(1)
                else:
                    new_row.append(triangle[i][pre] + triangle[i][next])
                    pre += 1
                    next = pre + 1
            triangle.append(new_row)


        return triangle
