import Event
from Date import *
import os
#FIXME I have not yet tested this class
class Planner:
    #TODO simiplify
    def __init__(self,UserName) -> None:
        id = -1
        if not os.path.exists(f'events\{UserName}'):
            os.makedirs(f'events\{UserName}')
        for i in os.listdir(f'events\\{UserName}'):
            if id < int(i.split('.')[0]):
                id = int(i.split('.')[0])
        self.maxid = id
        self.Events = []
        if id > -1:
            for i in range(0,id+1):
                self.Events.append(Event.Event(i))
        self.username = UserName
        pass
    #TODO Simplify
    def addEvent(self,startDT:DateTime, endDT:DateTime,EventName = "",description = "",location = "",UserName = "DefaultName"):
        self.Events.append(Event.Event(self.maxid+1,EventName,description,location,UserName,startDT=startDT,endDT=endDT))
        self.maxid += 1
    #TODO simplify
    def deleteEvent(self,id):
        os.remove(f'events\{self.username}\{id}.pkl')
        id += 1
        while id <= self.maxid:
            os.rename(f'events\{self.username}\{id}.pkl',f'events\{self.username}\{id-1}.pkl')
        self.maxid -= 1
        self.Events = []
        if self.maxid > -1:
            for i in range(0,self.maxid+1):
                self.Events.append(Event.Event(i))
i = Planner("Nate")
#helo