import Event
from Date import *
import os
#FIXME I have not yet tested this class
class Planner:
    #TODO simiplify
    def __init__(self,UserName) -> None:
        self.startUp()
        pass
    def startUp(self,UserName):
        """Used during start up and when an event is deleted to load the events"""
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
    #TODO Simplify
    def addEvent(self,startDT:DateTime, endDT:DateTime,EventName = "",description = "",location = "",UserName = "DefaultName"):
        self.Events.append(Event.Event(self.maxid+1,EventName,description,location,UserName,startDT=startDT,endDT=endDT))
        self.maxid += 1
    #TODO simplify
    def deleteEvent(self,id):
        self.Events[id].deleteSelf(id)
        self.startUp(self.username)
    #TODO Create a Modify for each aspect of Event
    def changeEndDate(self,id,datetime):
        self.Events[id].setEndDateTime(datetime)
    def changeStartDate(self,id,datetime):
        self.Events[id].setStartDateTime(datetime)
    def changeEventName(self,id,name):
        self.Events[id].setEventName(name)
    def setDescription(self,id,desc):
        self.Events[id].setDescription(desc)
    def setLocation(self,id,location):
        self.Events[id].setLocation(location)