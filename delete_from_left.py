#!/usr/bin/python3

# def delete_from_left(s, t):
#     """finds the minimum number of moves to make two given strings s and t equal."""
#     moves = 0
#     while s != t:
#         if len(s) == len(t):
#             s = s[1:]
#             t = t[1:]
#             moves += 2
#         else:
#             while len(s) > len(t):
#                 s = s[1:]
#                 moves += 1
#             while len(s) < len(t):
#                 t = t[1:]
#                 moves += 1

#     return moves

# s = input().lower()
# t = input().lower()

# print(delete_from_left(s, t))

def delete_from_left(s, t):

    common_suffix_len = 0
    min_len = min(len(s), len(t))
    
    for i in range(1, min_len + 1):
        if s[-i] == t[-i]:
            common_suffix_len += 1
        else:
            break
    
    moves = (len(s) - common_suffix_len) + (len(t) - common_suffix_len)
    
    return moves

s = input()
t = input()

print(delete_from_left(s, t))
