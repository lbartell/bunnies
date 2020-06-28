"""
Solution to: En Route Salute
"""


def solution(hallway):
    """counts how many salutes are exchanged during a typical walk along a hallway.

    Args:
        hallway: string representation of hallway with "-", "<", and ">" characters, length [1, 100]

    Returns:
        integer number of salutes
    """
    salutes = 0

    for index, step in enumerate(hallway):
        if step == ">":
            for val_to_right in hallway[index:]:
                if val_to_right == "<":
                    salutes += 1

        if step == "<":
            for val_to_left in hallway[:index]:
                if val_to_left == ">":
                    salutes += 1

    return salutes
