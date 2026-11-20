from itertools import combinations, product
from enum import Enum
import heapq

sessions = ["Poetry", "Music", "History"]
days = ["Mon", "Tue"]
rooms = ["A", "B"]
requests = [(2, 0, "Poetry"), (1, 1, "Music"), (2, 2, "History")]

# TODO: count session pairs and day/room choices.
# TODO: define State and initialize each session as PENDING.
# TODO: process requests by priority and arrival, marking each SCHEDULED.
# TODO: print the results specified in the book and check all states.
