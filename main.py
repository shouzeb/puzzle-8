# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 21:30:56 2020

@author: Shouzeb
"""

from puzzle import Runner
from time import time
from BFS_search import Breath_First_Search
from DFS_search import depth_first_search
from Astar_search import Astar_Search
from greedy_search import Greedy_Search
from uniform_cost_search import uniform_cost_search
state=[7,5,2,4,0,8,6,1,3]


print("\t\t\t>>>>>>Implementating Astar Search. Kindly wait...<<<<<<")
Runner.number_of_steps=0
t0=time()
Astar=Astar_Search(state)
t1=time()-t0
print('Astar:', Astar)
print('space:',Runner.number_of_steps)
print('time:',t1)
print()
print("\t\t\t>>>>>>Implementating Greedy Search. Kindly wait...<<<<<<")
Runner.number_of_steps=0
t0=time()
greedy=Greedy_Search(state)
t1=time()-t0
print('Greedy:', greedy)
print('space:',Runner.number_of_steps)
print('time:',t1)
print()
print("\t\t\t>>>>>>Implementating Unifrom Cost Search. Kindly wait...<<<<<<")
Runner.number_of_steps=0
t0=time()
ufs=uniform_cost_search(state)
t1=time()-t0
print('Uniform Cost Search:', ufs)
print('space:',Runner.number_of_steps)
print('time:',t1)
print()

print("\t\t\t>>>>>>Implementating Breath First Search. Kindly wait...<<<<<<")
Runner.number_of_steps=0
t0=time()
bfs=Breath_First_Search(state)
t1=time()-t0
print('BFS:', bfs)
print('space:',Runner.number_of_steps)
print('time:',t1)
print()
print("\t\t\t>>>>>>Implementating Deapth First Search. Kindly wait...<<<<<<")
Runner.number_of_steps=0
t0=time()
dfs=depth_first_search(state)
t1=time()-t0
print('DFS:', dfs)
print('space:',Runner.number_of_steps)
print('time:',t1)
print()