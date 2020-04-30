# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 23:22:25 2020

@author: Shouzeb
"""

from puzzle import Runner
from queue import Queue

def Breath_First_Search(initial_state):
    start_node = Runner(initial_state, None, None,0)
    if start_node.goal_state_check():
        return start_node.find_solution_path()
    q=Queue()
    q.put(start_node)
    explored=[]
    while not(q.empty()):
        node=q.get()
        explored.append(q)
        children=node.generate_child()
        #print(children)
        for child in children:
            #print(str(child))
            if child.state not in explored:
                if child.goal_state_check():
                    print("i am here")
                    return child.find_solution_path()
                q.put(child)
    return
        
    
    