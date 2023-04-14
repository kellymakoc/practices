#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMinCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY val
#  2. UNWEIGHTED_INTEGER_GRAPH t
#

#
# For the unweighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i].
#
#

def getMinCost(val, t_nodes, t_from, t_to):
    # Write your code here
    
    for i in range(t_nodes):
        val[i] = val[i] % 2
    
    adj = [set() for i in range(t_nodes)] # create each val with their own list with neighbours
    
    for i in range (len(t_from)): #searching their neighbours
        adj[t_from[i]-1].add(t_to[i]-1)
        adj[t_to[i]-1].add(t_from[i]-1)
        
    # leaves or parents
    leaves = []
    for i in range(t_nodes):
        if len(adj[i]) == 1: # there is no child (leaf)
            leaves.append(i)
        
    
    # iterate the leaves and find the parent
    remaining = t_nodes
    total_cost = 0
    
    while (leaves and remaining > 2): # there will only be 2 nodes and 1 edge left at the end
        remaining -= len(leaves)
        newLeaves = [] #updated leave list after removing the leaves 
        for leaf in leaves:
            parent = adj[leaf].pop() #get the parent node
            adj[parent].remove(leaf) # after removing leave, check if parent has any more child
            
            #leaf is 1 or 0, if 1, then invert parent (cost++)
            if val[leaf] == 1:
                total_cost += 1
                val[parent] = 1 - val[parent]
                
            #check if parent has other child
            if len(adj[parent]) == 1:
                newLeaves.append(parent)
        
        leaves = newLeaves #update the leave list with 'new' leaves
        
    #finally checks the last 2 nodes
    if leaves and val[leaves[0]] == 1:
        total_cost += 1
        
    return total_cost
        
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    val_count = int(input().strip())

    val = []

    for _ in range(val_count):
        val_item = int(input().strip())
        val.append(val_item)

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    result = getMinCost(val, t_nodes, t_from, t_to)

    fptr.write(str(result) + '\n')

    fptr.close()
