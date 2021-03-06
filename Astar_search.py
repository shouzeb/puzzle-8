# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:14:30 2020

@author: Shouzeb
"""

from queue import PriorityQueue
from puzzle import Runner

def Astar_Search(starting_node):
    count=0
    fringe=[]
    start_node=Runner(starting_node, None, None, 0, True,False,False)
    q=PriorityQueue()
    q.put((start_node.function,count,start_node))
    while not q.empty():
        #print("i am here")
        node=q.get()
        node=node[2]
        fringe.append(node.state)
        if node.goal_state_check():
            return node.find_solution_path()
        children=node.generate_child()
        for child in children:
            if child.state not in fringe:
                count+=1
                #print("count is ",count," evaluation function is ",child.function)
                #print(child)
                q.put((child.function,count,child))
    return