"""
Solution to: Running with Bunnies
"""
from collections import deque
from copy import deepcopy

class Node(object):

    def __init__(self, position, time_costs, is_end=False):
        self.nodes = []
        self.position = position
        self.time_costs = time_costs
        self.to_end_cost = time_costs[-1]
        self.is_end = is_end

    def is_valid_terminal_node(self, time_remaining):
        return not self.is_end and time_remaining >= self.to_end_cost

    def optimal_child_path(self, time_remaining, previously_visited):
        visited = deepcopy(previously_visited)
        visited[self.position] += 1
        count_visited = sum([1 for x in visited[1:-1] if x > 0])
        optimal = None

        # awful cycle detection check
        if visited[self.position] < 10:
            for node in self.nodes:
                # don't stand still
                if node.position != self.position:
                    # get the best path starting with that node
                    node_optimal, child_visited_count = node.optimal_child_path(time_remaining - self.time_costs[node.position], visited)
                    # if there is a valid path, and it has a greater number of bunnies visited, take that
                    # *not* greater than or equal number of bunnies, that way we will always return the lowest index bunnies for equal paths
                    # assuming we iterate in order
                    if node_optimal is not None and child_visited_count > count_visited:
                        optimal = node_optimal
                        optimal.appendleft(self.position)
                        count_visited = child_visited_count

        # if nothing has been found so far, the optimal path is the one that ends here, or this is a dead leaf
        if optimal is None and self.is_valid_terminal_node(time_remaining):
            optimal = deque([self.position])

        return optimal, count_visited

class Graph(object):
    def __init__(self, times, time_limit):
        # assume to be square
        self.dimension = len(times)
        self.time_limit = time_limit
        self.nodes = []
        self.valid_sequences = []
        # make a node for each row, since the rows correspond to each position
        for i in range(self.dimension):
            self.nodes.append(Node(i, times[i], i == self.dimension - 1))

        # add references to the other nodes because this is a fully connected graph (complete graph)
        # this way we can traverse the graph from any individual node
        for i in range(self.dimension):
            for j in range(self.dimension):
                self.nodes[i].nodes.append(self.nodes[j])

    def brute(self):
        # count how many times we've visited each node
        visited = [1]
        for i in range(self.dimension - 1):
            visited.append(0)

        # start from the starting position, i.e. node[0]
        optimal, count_visited = self.nodes[0].optimal_child_path(self.time_limit, visited)

        # convert the paths into bunny prisoner numbers
        # bunnies are zero-indexed from position 1 in the zero-indexed node list
        # skip nodes 0 and -1 because they are the start and bulkhead
        bunnies = []
        for i in range(1, self.dimension - 1):
            if i in optimal:
                bunnies.append(i - 1)
        return bunnies



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
            # - go back to the start if it costs time
            same_spot = next_step == self.current_index
            saved_bunny = next_step in self.saved_bunny_indices
            costs_time = self.times[self.current_index][next_step] > self.current_time
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
    return JmSolve(times, time_limit)

def JmSolve(times, time_limit):
    return Graph(times, time_limit).brute()

def LenaSolve(times, time_limit):
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
