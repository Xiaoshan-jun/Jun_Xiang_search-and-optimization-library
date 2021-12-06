# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 03:03:05 2021
A* search
@author: jun xiang
"""
import numpy as np

class node:
    def __init__(self, mark, avaliable, cost, h, gh):
        self.mark = mark #mark is the label of a node
        self.avaliable = avaliable #list of mark of nodes the current node can reach
        self.cost = cost #cost of reaching this node
        self.h = h #heuristic value, defined manually
        self.gh = gh #record lowest cost reach this node, use for search
        self.path = [] #the best path to reach the node
        
#Queue save node needed to be explore, sorted by gh value.
class PriorityQueue:
    def __init__(self, NodeList):
        self.queue = []
        self._index = 0
        self.NodeList = NodeList

    def insert(self, node):
        last = True
        for i in range(len(self.queue)):
            if self.NodeList[self.queue[i]].gh > node.gh:
                self.queue.insert(i, node.mark)
                last = False
                self._index += 1
        if last:
            self.queue.append(node.mark)
            self._index += 1

    def pop(self):
        self._index -= 1
        return self.queue.pop(0)
        
def search(frontier, explored, NodeList):
    while True:
        if frontier._index == 0:
            return False, False
        node = NodeList[frontier.pop()]
        if node.mark == 8:
            return node.path, node.gh
        explored.append(node.mark)
        for mark in node.avaliable:
            child = NodeList[mark]
            if mark not in frontier.queue or mark not in explored :
                child.gh = node.gh + node.cost[node.avaliable.index(mark)] + child.h
                child.path = node.path.copy()
                child.path.append(child.mark)
                frontier.insert(child)
            elif mark in frontier.queue:
                #update new path if new path is closer
                if node.gh + node.cost[node.avaliable.index(mark)] + child.h < child.gh: 
                    child.gh = node.gh + node.cost[node.avaliable.index(mark)] + child.h
                    child.path = node.path 
                    child.path.append(child.mark)
#define h value
h = np.array([0,1,1,1,2,2,2,2,0])
#------------------create node---------------
Node0 = node(0,[1,2,3,4],[10,8,6,4],h[0], 0)
Node1 = node(1,[5],[2],h[1], 1000)
Node2 = node(2,[3,5],[1,8],h[2], 1000)
Node3 = node(3,[6],[4],h[3], 1000)
Node4 = node(4,[6,7],[5,2],h[4], 1000)
Node5 = node(5,[8],[6],h[5], 1000)
Node6 = node(6,[8],[4],h[6], 1000)
Node7 = node(7,[8],[2],h[7], 1000)
Node8 = node(8,[],[],h[8], 0)
#------------------create node---------------
NodeList = [Node0,Node1,Node2,Node3,Node4,Node5,Node6,Node7,Node8]
Node0.path = [0] 
path = [0] 
frontier = PriorityQueue(NodeList) #create queue
frontier.insert(Node0) #insert start node
explored = []
path, cost= search(frontier, explored, NodeList) #search tghe path

print(path)


