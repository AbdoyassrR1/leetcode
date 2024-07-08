#!/usr/bin/python3

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len((s.split())[-1])
