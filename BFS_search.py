# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 23:22:25 2020

@author: Shouzeb
"""

from puzzle import Runner
from queue import Queue

def Breath_First_Search(initial_state):
    start_node = Runner(initial_state, None, None,0,False,False,False)
    if start_node.goal_state_check():
        return start_node.find_solution_path()
    q=Queue()
    q.put(start_node)
    fringe=[]
    while not(q.empty()):
        node=q.get()
        fringe.append(q)
        children=node.generate_child()
        #print(children)
        for child in children:
            #print(str(child))
            if child.state not in fringe:
                
                if child.goal_state_check():
                    return child.find_solution_path()
                q.put(child)
    return
        
    
    