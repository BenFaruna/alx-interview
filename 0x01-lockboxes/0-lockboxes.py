#!/usr/bin/python3
"""LockBoxes Algorithm"""
def canUnlockAll(boxes):
    """determine if all boxes can be opened"""
    unlocked = [0]
    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
