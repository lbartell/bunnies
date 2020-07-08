"""
Solution to: The Grandest Staircase Of Them All
"""
from collections import deque


class Path(object):

    def __init__(self, times, path_indices, current_time):
        self.times = times
        self.path_indices = path_indices
        self.current_time = current_time

        # Derived quantities
        self.current_index = self.path_indices[-1]
        self.num_positions = len(self.times)
        self.all_bunny_indices = set(range(1, self.num_positions - 1))
        self.saved_bunny_indices = self.all_bunny_indices.intersection(self.path_indices)
        self.saved_bunnies = set([index - 1 for index in self.saved_bunny_indices])
        self.at_bulkhead = self.current_index == self.num_positions - 1
        self.all_bunnies_saved = not self.all_bunny_indices - self.saved_bunny_indices
        self.is_valid_path = self.at_bulkhead and self.current_time >= 0

    def branches(self):
        branched_paths = list()

        for next_step in range(self.num_positions):

            # Exit conditions: Don't..
            # - stay in the same spot
            # - try to save a bunny that was already saved
            # - go to a non-bunny spot that costs time
            same_spot = next_step == self.current_index
            saved_bunny = next_step in self.saved_bunny_indices
            costs_time = self.times[self.current_index][next_step] > 0
            costly_back_to_start = next_step == 0 and costs_time

            if not same_spot and not saved_bunny and not costly_back_to_start:
                new_path = self.path_indices + [next_step]
                branched_paths.append(
                    Path(
                        times=self.times,
                        path_indices=new_path,
                        current_time=self.current_time - self.times[self.current_index][next_step]
                    )
                )

        return branched_paths


def solution(times, time_limit):
    """Calculate the most bunnies you can pick up and which bunnies they are

        [
          [0, 2, 2, 2, -1],  # 0 = Start
          [9, 0, 2, 2, -1],  # 1 = Bunny 0
          [9, 3, 0, 2, -1],  # 2 = Bunny 1
          [9, 3, 2, 0, -1],  # 3 = Bunny 2
          [9, 3, 2, 2,  0],  # 4 = Bulkhead
        ]

    Args:
        times: 2D array of int; time it takes to move from your starting point to all of the bunnies and to the bulkhead
        time_limit: int, time limit before bulkhead closes

    Returns:
        list of integers specifying which bunnies to save
    """
    paths = deque([Path(times=times, path_indices=[0], current_time=time_limit)])
    valid_paths = []

    while paths:

        current_path = paths.popleft()

        paths.extend(current_path.branches())

        if current_path.is_valid_path:
            valid_paths.append(current_path)

            if current_path.all_bunnies_saved:
                break

    sorted_paths = sorted(
        valid_paths,
        key=lambda p: (len(p.saved_bunny_indices), - sum(p.saved_bunny_indices)),
        reverse=True
    )

    saved_bunnies = list(sorted_paths[0].saved_bunnies)

    return saved_bunnies
