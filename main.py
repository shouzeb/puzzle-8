# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 22:53:16 2020

@author: Shouzeb
"""


__Project_Description__ = '''
This is a python based 3x3 puzzle solver which solves the problem by using list
which represented as 1 dimensionally. (Using 1D list is the greatest challenge for me.)
Project has several methods to solve subproblems. The subproblems are:
    * Calculating inversion,
    * Checking solubility of the board,
    * Calculating Hamming Distance,
    * Calculating Manhattan Distance (BONUS),
    * If board arrangement has solution than find the 'Legal Board Arrangements' -> (changing blank tile's position)
    * Generate a heuristic function to get closest path to go to goal state.
    * Breadth First Search and Generating the Result.'''

from time import time
from BFS_search import breadth_first_search
from Astar_search import Astar_search
from RBFS_search import recursive_best_first_search
from puzzle import Runner


state=[[1 , 2, 0, 3, 4, 5, 6, 7, 8]]

for i in range(0,1):
    Runner.num_of_instances=0
    t0=time()
    bfs=breadth_first_search(state[i])
    t1=time()-t0
    print('BFS:', bfs)
    print('space:',Runner.num_of_instances)
    print('time:',t1)
    print()

    Runner.num_of_instances = 0
    t0 = time()
    astar = Astar_search(state[i])
    t1 = time() - t0
    print('A*:',astar)
    print('space:', Runner.num_of_instances)
    print('time:', t1)
    print()

    Runner.num_of_instances = 0
    t0 = time()
    RBFS = recursive_best_first_search(state[i])
    t1 = time() - t0
    print('RBFS:',RBFS)
    print('space:', Runner.num_of_instances)
    print('time:', t1)
    print()
    
    print('------------------------------------------')