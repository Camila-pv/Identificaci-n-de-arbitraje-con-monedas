from numpy import genfromtxt
import numpy as np
import math
from numpy import loadtxt

data = loadtxt('ARB.txt')

# Function to print adjacency list representation of a graph
dic = { 0:'USD',1:'EUR',2:'JPY',3:'GBP',4:'CAD',5:'AUD',6:'NZD',7:'CHF',8:'DKK',9:'NOK',10:'SEK'}


class Graph:
 
    def __init__(self):
        self.V = len(data) # No. of vertices
        self.graph = []

        for u in range(self.V):
            for v in range(self.V):
                if u!=v:
                    self.graph.append([u, v, -math.log(data[u][v])])
         
    # utility function used to print the solution
    def printArr(self, dist,src):
        print("Vertex Distance from Source ", dic[src] )
        for i in range(self.V):
            print("{0}\t\t{1}".format(dic[i], dist[i]))
        print('\n')
     
    # The main function that finds shortest distances from src to
    # all other vertices using Bellman-Ford algorithm. The function
    # also detects negative weight cycle
            

        
    def BellmanFord(self):
    
        
 
        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        source = 0
        dist = [float("Inf")] * self.V
        pre = [-1]*self.V
        dist[source] = source
 
 
        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1
        # edges
        for _ in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    pre[v]=u
 
        # Step 3: check for negative-weight cycles. The above step
        # guarantees shortest distances if graph doesn't contain
        # negative weight cycle. If we get a shorter path, then there
        # is a cycle.
        for u, v, w in self.graph:
            
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print_cycle = [v,u]
                while pre[u] not in print_cycle:
                    print_cycle.append(pre[u])
                    u =pre[u]
                print_cycle.append(pre[u])
                
                if print_cycle[0]==print_cycle[-1]:
                    u = 1
                    for p in range(len(print_cycle[::-1][:-1])):
                        
                        #print(print_cycle[::-1][p],print_cycle[::-1][p+1])
                        
                        u = data[print_cycle[::-1][p+1]][print_cycle[::-1][p]] * u
                        
                    r =(u/1 -1)*100
                    
                    
                    if(r>0 and r<1):
                        print("arbitraje*: ")
                    #print(print_cycle)
                        print(" --> ".join([dic[p] for p in print_cycle[::-1]]))
                        print(r,"%")
                        
                    
                else:
                   
                    #print(print_cycle)
                    print_cycle = [print_cycle[-1], *print_cycle]
                    
                    u = 1
                    for p in range(len(print_cycle[::-1][:-1])):
                        
                        #print(print_cycle[::-1][p],print_cycle[::-1][p+1])
                        
                        u = data[print_cycle[::-1][p+1]][print_cycle[::-1][p]] * u
                        
                    r =(u/1 -1)*100

                    
                    if(r>0 and r<1):
                        print("arbitraje: ")
                    #print(print_cycle)
                        print(" --> ".join([dic[p] for p in print_cycle[::-1]]))
                        print(r,"%")
                       
                        
                        
                    #print(u)
                    
                        
                       
                    
                    
               
                
               
            
            
                         
        # print all distance
            

 

if __name__ == '__main__':

    g = Graph()
    g.BellmanFord()
    

    
    
