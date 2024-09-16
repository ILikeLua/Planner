from Date import *
import os
import pickle
#keeps track of events
class Event:
    #constructor
    def __init__(self,id:int,EventName = "",description = "",location = "",UserName = "DefaultName",*,startDT:DateTime, endDT:DateTime):
        #TODO: Ensure that the id is unique to the username and throw an error if it isn't
        if self.load(UserName,id):
            return 
        for i in [1,2,3,4,5,6,7,8,9,0]:
            EventName = EventName.replace(str(i),'')
        self.start = startDT
        self.end = endDT
        self.EventName, self.description, self.location = EventName, description, location
        #unique identifier of this event. used for updating
        self.id = id
        self.UserName = UserName
        self.save()
    def __str__(self) -> str:
        return f'Start Time:\n{str(self.start)}\n---\nEnd Time:\n{str(self.end)}\n---\nEvent Name:\n{self.EventName}\n---\nDescription:\n{self.description}\n---\nLocation:\n{self.location}\n---\nId:\n{self.id}\n---\nUserId:\n{self.UserName}'
    def getEndTime(self) -> Time:
        return self.end
    def getStartTime(self) -> Time:
        return self.start
    def getEventName(self) -> str:
        return self.EventName
    def getDescription(self) -> str:
        return self.description
    def getLocation(self) -> str:
        return self.location
    def getId(self) -> int:
        return self.id
    def getUserName(self) -> str:
        return self.UserName
    #lets you update datetime
    def setEnd(self,minute = -1,hour = -1,day = -1,Month = -1,Year = -1) -> None:
        #TODO make sure that the end can't be before the start
        if minute != -1:
            self.end.time.Minute = minute
        if hour != -1:
            self.end.time.Hour = hour
        if day != -1:
            self.end.date.Day = day
        if Month != -1:
            self.end.date.Month = Month
        if Year != -1:
            self.end.date.Year = Year
        self.save()
    def setStart(self,minute = -1,hour = -1,day = -1,Month = -1,Year = -1) -> None:
        #TODO Make sure that the start can't be after the end. maybe set a comparison between the two types?
        if minute != -1:
            self.start.time.Minute = minute
        if hour != -1:
            self.start.time.Hour = hour
        if day != -1:
            self.start.date.Day = day
        if Month != -1:
            self.start.date.Month = Month
        if Year != -1:
            self.start.date.Year = Year
        self.save()
    def setEventName(self,EventName) -> None:
        for i in [1,2,3,4,5,6,7,8,9,0]:
            EventName = EventName.replace(str(i),'')
        self.EventName = EventName
        self.save()
    def setDescription(self,Description) -> None:
        self.description = Description
    def setLocation(self,Location) -> None:
        self.location = Location
    #If it returns false there is no file to load, if true a file was loaded
    def load(self,UserName,id) -> bool:

        if not os.path.exists(f'events\\{UserName}\\{id}.pkl'):
            return False
        print("hi")
        with open(f'events\\{UserName}\\{id}.pkl',"rb") as i:
            self.start,self.end,self.EventName,self.description,self.location,self.id,self.UserName = pickle.load(i)
        return True

    def save(self):
        if not os.path.exists(f'events\{self.UserName}'):
            os.makedirs(f'events\{self.UserName}')
        with open(f'events\\{self.UserName}\\{self.id}.pkl', 'wb') as i:
            pickle.dump([self.start,self.end,self.EventName,self.description,self.location,self.id,self.UserName],i)
        pass