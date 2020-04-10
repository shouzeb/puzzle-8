# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 15:18:55 2020

@author: Shouzeb
"""

from queue import Queue
from puzzle import Runner


def depth_first_search(initial_state):
    start_node = Runner(initial_state, None, None, 0)
    if start_node.goal_test():
        return start_node.find_solution()
    q = Queue()
    q.put(start_node)
    explored=[]
    while not(q.empty()):
        node=q.get(q.qsize()-1)
        explored.append(node.state)
        children=node.generate_child()
        print(children)
        for child in children:
            if child.state not in explored:
                if child.goal_test():
                    return child.find_solution()
                q.put(child)
    return
