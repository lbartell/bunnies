"""
Solution to: The Grandest Staircase Of Them All
"""
from collections import deque


class Path(object):

    def __init__(self, times, path_indices):
        self.times = times
        self.path_indices = path_indices

        # Derived properties
        self.num_positions = len(self.times)
        self.all_bunny_indices = set(range(1, self.num_positions - 1))
        self.current_index = self.path_indices[-1]

        self.saved_bunny_indices = self._get_saved_bunny_indices()
        self.total_time = self._get_total_time()

        self.at_bulkhead = self.current_index == self.num_positions - 1
        self.all_bunnies_saved = not self.all_bunny_indices - self.saved_bunny_indices

    def _get_saved_bunny_indices(self):
        saved_bunny_indices = set()
        for index in self.path_indices:
            if 0 < index < self.num_positions:
                saved_bunny_indices.add(index)
        return saved_bunny_indices

    def _get_total_time(self):
        total_time = 1
        for start_index, end_index in zip(self.path_indices[:-1], self.path_indices[1:]):
            total_time += self.times[start_index][end_index]
        return total_time

    def branches(self):
        branched_paths = list()

        for next_step in range(self.num_positions):
            # Don't stay in the same spot or try to save a bunny that is already saved
            if next_step not in self.saved_bunny_indices and next_step != self.current_index:
                new_path = self.path_indices + [next_step]
                branched_paths.append(new_path)

        return [Path(self.times, steps) for steps in branched_paths]


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
    paths = deque([Path(times, [0])])
    valid_paths = []

    while paths:

        current_path = paths.popleft()

        paths.extend(current_path.branches())

        if current_path.at_bulkhead and current_path.total_time <= time_limit:
            valid_paths.append(current_path)

    sorted_paths = sorted(
        valid_paths,
        key=lambda p: (len(p.saved_bunny_indices), sum(p.saved_bunny_indices))
    )

    saved_bunnies = [index - 1 for index in sorted_paths[0].saved_bunny_indices]
    return saved_bunnies
