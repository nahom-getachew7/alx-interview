#!/usr/bin/python3
"""
    This module contains the canUnlockAll function.
"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened
        Arg:
            boxes: Is a list of lists.
    """
    box = len(boxes) * [False]
    box[0] = True
    keys = [0]

    for each in keys:
        for i in boxes[each]:
            if i not in keys:
                if i < len(boxes):
                    box[i] = True
                    keys.append(i)
    return all(box)
