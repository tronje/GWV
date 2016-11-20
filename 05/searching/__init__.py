# -*- coding: utf-8 -*-
from .searching import bfs, dfs, astar
from .heuristics import h_distance

# supported searches
searches = {'bfs': bfs, 'dfs': dfs, 'astar': astar}

# supported heuristic functions
heuristics = {'distance': h_distance}
