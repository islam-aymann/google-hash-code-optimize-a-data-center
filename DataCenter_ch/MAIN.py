#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 09:14:48 2018

@author: chaymae
"""

class server:
    def __init__(self,key,size,capacity):
        self.id = key
        self.size = size
        self.capacity= capacity
        self.capTsize = self.capacity/self.size
        self.capVsize = self.capacity * self.size
    def getSize(self):
        return self.size
    def getCap(self):
        return self.capacity
    def capTsize(self):
        return self.capTsize
    def capVsize(self):
        return self.capVsize
    def __str__(self):
        return "Server: "+ str(self.id) + "," + "Cap: " + str(self.capacity) + "," + "size: " + str(self.size)+"\n" 
    


class DataCenter:
    def __init__(self,):
        self.checking=list()

    def readFile(self):
        data = open("dc.in")
        self.servers=list()
        self.rows, self.slots, self.slots_Un, self.pools,self.numb_servers = (map(int, data.readline().strip().split()))
        
        for i in range(self.rows):
            self.checking.append([-1]*(self.slots))
        for i in range(self.slots_Un):
            UnavailbleX,UnavailbleY=map(int, data.readline().strip().split())
            self.checking[UnavailbleX][UnavailbleY]=-2
           
        for i in range(self.numb_servers):            
            size,capacity=map(int, data.readline().strip().split())
            new_server=server(i,size,capacity)
            self.servers.append(new_server)
        data.close()
        
        

            
    def sort(self,key,rev=True):
        return sorted(self.servers,key=key,reverse=rev)
    

    
    def put_servers(self,keyForSorting):
        self.sheet=list()
        self.failures=dict()
        self.poolCapacities=dict()
        sortedLst=self.sort(keyForSorting)
        self.row=-1
        self.pool=0
        for serv in sortedLst:             
            if self.getNext(serv): #a sever has faied in all rows
                break
            else:
                if self.end>=self.slots:
                    self.failures[serv.id]=self.failures.get(serv.id,0)+1 #number of failures
                    if self.getNext(serv):
                        break
                else:
                    
                    self.pool+=1
                    if self.pool==self.pools:
                        self.pool=1
                    
                    self.poolCapacities[self.pool]=self.poolCapacities.get(self.pool,0)+1
                    self.sheet.append([serv.id,self.row,self.start,self.pool])
                    self.set_piece((serv.id,self.pool,serv.capacity),self.row,self.start,self.end)

#            print(self.start)
#            print(self.end)
#            print(self.row)
#            print(self.rows)
#            print(self.failures)
                
    def getNext(self,serv):
             
        
        self.row+=1
        if self.row==self.rows:
                self.row=0

        if -1 in self.checking[self.row]:
            self.start=self.checking[self.row].index(-1)  
            self.end=self.start+ serv.getSize()-1
            
        else:
            self.failures[serv.id]=self.failures.get(serv.id,0)+1 #number of failures
            if max(self.failures.values()) == self.rows:
                return True
            else:
                self.getNext(serv)
                return False

       
        
    def set_piece(self,setter, row, y1, y2):        
        for j in range(y1, y2+1):
            self.checking[row][j] = setter
        return True
            
def main():       
    center1=DataCenter()
    center1.readFile()
#    mysorted=center1.sort(server.getCap)
#    print(*mysorted)
    
    center1.put_servers(server.getCap)
#    print(center1.checking)
    out=sorted(center1.sheet)
    fo = open("output1.txt", "w")
    for i in out:                   
        fo.write(" ".join(map(str,i[1:])) + "\n")
    fo.close()

    center2=DataCenter()
    center2.readFile()    
    center2.put_servers(server.getSize)
    out=sorted(center2.sheet)
    fo = open("output2.txt", "w")
    for i in out:                   
        fo.write(" ".join(map(str,i[1:])) + "\n")
    fo.close()

    center3=DataCenter()
    center3.readFile()    
    center3.put_servers(server.capTsize)
    out=sorted(center3.sheet)
    fo = open("output3.txt", "w")
    for i in out:                   
        fo.write(" ".join(map(str,i[1:])) + "\n")
    fo.close()

    center4=DataCenter()
    center4.readFile()    
    center4.put_servers(server.capVsize)
    out=sorted(center4.sheet)
    fo = open("output4.txt", "w")
    for i in out:                   
        fo.write(" ".join(map(str,i[1:])) + "\n")
    fo.close()
    
#    print(*center.servers)


if __name__ == '__main__':
    print('Starting...')
    main()
    print('\nEnd...')

