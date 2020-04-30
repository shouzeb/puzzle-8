# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:27:44 2020

@author: Shouzeb
"""
from queue import PriorityQueue
from puzzle import Runner

def Greedy_Search(starting_node):
    count=0 #indicates how many nodes have been trasversed
    fringe=[]
    start_node=Runner(starting_node, None, None, 0, False,True,False)
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