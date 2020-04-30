# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 21:31:56 2020

@author: Shouzeb
"""

class Runner:
    goal_state=[0,1,2,3,4,5,6,7,8]
    number_of_steps=0
    heuristic_required_Astar=None
    heuristic_required_Greedy=None
    heuristic_required_ufs=None
    function=None
    heuristic=None
    def __init__(self,state,parent,action,path_cost,heuristic_required_Astar=False,heuristic_required_Greedy=False,heuristic_required_ufs=False):
        
        self.parent=parent
        self.state=state
        self.action=action
        if parent:
            self.path_cost=parent.path_cost+path_cost
        else:
            self.path_cost=path_cost
        if heuristic_required_Astar:
            self.heuristic_required_Astar=True
            self.generate_heuristic()
            self.function=self.heuristic+self.path_cost
            #print("astar heuristic")
        elif heuristic_required_Greedy:
            self.heuristic_required_Greedy=True
            self.generate_heuristic()
            self.function=self.heuristic
            #print("Greedy heuristic")
        elif heuristic_required_ufs:
            self.heuristic_required_ufs=True
            self.generate_heuristic()
            self.function=self.path_cost
            #print("UFS heuristic")
        
        Runner.number_of_steps+=1
    
    def __str__(self):
        return (str(self.state[0:3])+'\n'+str(self.state[3:6])+'\n'+str(self.state[6:9])+"\n")

    def goal_state_check(self):
        #print("i am here",self.state)
        
        if self.state==self.goal_state:
            return True
        return False
       
    @staticmethod
    def find_valid_moves(i,j):
        valid_moves=['U','D','L','R']
        if i == 0:  # up is disable
            valid_moves.remove('U')
        elif i == 2:  # down is disable
            valid_moves.remove('D')
        if j == 0:
            valid_moves.remove('L')
        elif j == 2:
            valid_moves.remove('R')
        return valid_moves
            
    
    def generate_child(self):
        children=[]
        x=self.state.index(0)
        
        i=int(x/3)
        j=int(x%3)
        valid_moves=self.find_valid_moves(i,j)
        #print(valid_moves)
        for move in valid_moves:
            new_state=self.state.copy()
            if move == 'U':
                new_state[x], new_state[x-3] = new_state[x-3], new_state[x]
            elif move == 'D':
                new_state[x], new_state[x+3] = new_state[x+3], new_state[x]
            elif move == 'L':
                new_state[x], new_state[x-1] = new_state[x-1], new_state[x]
            elif move == 'R':
                new_state[x], new_state[x+1] = new_state[x+1], new_state[x]
            children.append(Runner(new_state,self,move,1,self.heuristic_required_Astar,self.heuristic_required_Greedy,self.heuristic_required_ufs))
        return children
    
    def generate_heuristic(self):
        self.heuristic=0
        for num in range(1,9):
            distance=abs(self.state.index(num)-self.goal_state.index(num))
            i=int(distance/3)
            j=int(distance%3)
            self.heuristic=self.heuristic+i+j
    
    def find_solution_path(self):
        solution=[]
        solution.append(self.action)
        path=self
        while path.parent != None:
            path=path.parent
            solution.append(path.action)
        solution=solution[:-1]
        solution.reverse()
        return solution
    
        
                
        
    