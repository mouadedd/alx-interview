#!/usr/bin/python3
'''Lock Boxes game'''


def canUnlockAll(boxes):
    '''
    lock boxes condition:
    Return:
        True: if all the boxes can be opened
        False: if not all the boxes can be opened
    '''
    length = len(boxes)
    keys = set()
    open_boxe = []
    idx = 0

    while idx < length:
        all_box = idx
        open_boxe.append(idx)
        keys.update(boxes[idx])
        for key in keys:
            if key != 0 and key < length and key not in open_boxe:
                idx = key
                break
        if all_box != idx:
            continue
        else:
            break

    for idx in range(length):
        if idx not in open_boxe and idx != 0:
            return False
    return True
