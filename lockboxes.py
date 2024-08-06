#!/usr/bin/python3
from typing import List


def canUnlockAll(boxes: List[List]) -> bool:
    all_boxes = len(boxes)
    keys = []
    print("keys", keys)
    index = 0
    for key in boxes[index]:
        keys.append(key)
    while index < len(keys):
        for key in boxes[keys[index]]:
            if key not in keys and key < all_boxes and key > 0:
                keys.append(key)
        index += 1
    print("keys", keys)
    if len(keys) == all_boxes - 1:
        return True
    else:
        return False

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
