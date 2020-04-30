# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 23:27:36 2020

@author: Shouzeb
"""
from puzzle import Runner

def depth_first_search(starting_state):
    start_node=Runner(starting_state,None,None,0,False,False,False)
    if start_node.goal_state_check():
        return start_node.find_solution_path()
    s=[]
    s.append(start_node)
    fringe=[]
    #fringe.put(start_node)
    while (len(s)!=0):
        node=s.pop()
        fringe.append(node.state)
        children=node.generate_child()
        for child in children:
            if child.state not in fringe and child.goal_state_check():
                return child.find_solution_path()
            s.append(child)
    return