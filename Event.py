from Date import *
import os
import pickle
#keeps track of events
class Event:
    """A class used to represent an event in a day.
    
    ...

    Attributes
    ----------
    start : DateTime
        start time of the event
    end : DateTime
        end time of the event
    eventName : str
        name of the event
    description : str
        description of the event
    location : str
        location of the event
    id : int
        unique identifier of the event. Is also the name of the file that the event is in
    userName : str
        name of the user who's event it is. Is also the folder the file the event is stored in.
    
    Methods
    ----------
    getEndTime() -> datetime
        get the end datetime of the event
    getStartTime() -> datetime
        get the start datetime of the event
    getEventName() -> str
        get the name of the event
    getDescription() -> str
        get the description of the event
    getLocation() -> str
        get the location of the event
    getId() -> int
        get the unique id of the event
    getUserName() -> str
        get the User of the event
    setEndDateTime(minute : int = -1, hour : int = -1, day : int = -1, Month : int = -1, Year : int = -1, fullDataTime : datetime = None) -> None
        updates the end datetime of the event
    setStartDateTime(minute : int = -1, hour : int = -1, day : int = -1, Month : int = -1, Year : int = -1, fullDataTime : datetime = None) -> 
        updates the end datetime of the event.
    setEventName(EventName: str)
        updates the event name
    setDescription(description : str)
        updates the description
    setLocation(Location : str)
        updates the Location
    loadEvent(UserName : str, Id: int)
        loads the file at relative path Events/<Username>/<Id>.pkl
        This automatically occures at initialization
    saveEvent()
        saves the file to relative path Events/<self.Username>/<self.Id>.pkl
    deleteSelf(MaxId)
        deletes self, updates next file's ids    """
    #constructor
    #TODO simiplify
    def __init__(self,id:int,eventName = "",description = "",location = "",userName = "DefaultName",startDT:DateTime = None, endDT:DateTime = None):
        """
        Parameters
        -----
        id : int
            Unique id of the event
        eventName : str = ""
            Name of the event
        description : str = ""
            Description of the event
        location : str = ""
            Location of the event
        userName : str = "DefaultName"
            User the event belongs to
        startDT : DateTime
            Start date of the event
        endDT : DateTime
            End date of the event
        """
        #TODO: Ensure that the id is unique to the username and throw an error if it isn't
        if self.loadEvent(userName,id):
            return 
        for i in [1,2,3,4,5,6,7,8,9,0]:
            eventName = eventName.replace(str(i),'')
        self.start = startDT
        self.end = endDT
        self.eventName, self.description, self.location = eventName, description, location
        #unique identifier of this event. used for updating
        self.id = id
        self.userName = userName
        self.saveEvent()
    def __str__(self) -> str:
        return self.eventName
    def getEndTime(self) -> Time:
        """
        Get the end datetime of the event
        """
        return self.end
    def getStartTime(self) -> Time:
        """
        Get the start datetime of the event
        """
        return self.start
    def getEventName(self) -> str:
        """
        Get the events name
        """
        return self.eventName
    def getDescription(self) -> str:
        """
        Gets the description of the event
        """
        return self.description
    def getLocation(self) -> str:
        """
        Gets the location of the event
        """
        return self.location
    def getId(self) -> int:
        """
        Gets the Unique Id of the event
        """
        return self.id
    def getUserName(self) -> str:
        """
        Gets the Username assosiated with the event
        """
        return self.userName
    #lets you update datetime
    def setEndDateTime(self,minute = -1,hour = -1,day = -1,month = -1,year = -1, *, fullDateTime:DateTime = None) -> None:
        """
        Sets the End DateTime of the event
        -----
        Parameters:
        Minute: int, optional
            Minute to change
        Hour : int, optional
            Hour to change
        Day : int, optional
            Day to change
        Month : int, optional
            Month to change
        Year : int, optional
            Year to change
        fullDateTime : int, optional
            The time to change to
        """
        #TODO make sure that the end can't be before the start
        if fullDateTime is not None:
            self.end = fullDateTime
            return
        self.end = DateTime(
            minute if minute != -1 else self.end.time.Minute,
            hour if hour != -1 else  self.end.time.Hour,
            day if day != -1 else self.end.date.Day,
            month if month != -1 else self.end.date.Month, 
            year if year != -1 else self.end.date.Year)
        self.saveEvent()
    def setStartDateTime(self,minute = -1,hour = -1,day = -1,month = -1,year = -1, *, fullDateTime:DateTime = None) -> None:
        """
        Sets the Start DateTime of the event
        -----
        Parameters:
        Minute: int, optional
            Minute to change
        Hour : int, optional
            Hour to change
        Day : int, optional
            Day to change
        Month : int, optional
            Month to change
        Year : int, optional
            Year to change
        fullDateTime : int, optional
            The time to change to
        """
        #TODO Make sure that the start can't be after the end. maybe set a comparison between the two types?
        if fullDateTime is not None:
            self.start = fullDateTime
            return
        self.start = DateTime(
            minute if minute != -1 else self.start.time.Minute,
            hour if hour != -1 else  self.start.time.Hour,
            day if day != -1 else self.start.date.Day,
            month if month != -1 else self.start.date.Month, 
            year if year != -1 else self.start.date.Year)
        self.saveEvent()
    def setEventName(self,EventName) -> None:
        """
        Sets the event name, gets rid of any numbers in the name
        -----
        Parameters:
        EventName: Str
            the name to change to
        """
        for i in [1,2,3,4,5,6,7,8,9,0]:
            EventName = EventName.replace(str(i),'')
        self.eventName = EventName
        self.saveEvent()
        
    def setDescription(self,Description) -> None:
        """
        Sets the description name
        -----
        description : str
            The description to change to
        """
        self.description = Description
        self.saveEvent()

    def setLocation(self,Location) -> None:
        """
        Sets the location
        -----
        Location: str
            The location to change to
        """
        self.location = Location
        self.saveEvent()

    #If it returns false there is no file to load, if true a file was loaded
    def loadEvent(self,UserName,id) -> bool:
        """
        loads the event for the username provided.
        -----
        UserName : str
            name of the username to load
        id : int
            the unique id to load
        """
        if not os.path.exists(f'events\\{UserName}\\{id}.pkl'):
            return False
        self.id = id
        with open(f'events\\{UserName}\\{id}.pkl',"rb") as i:
            self.start,self.end,self.eventName,self.description,self.location,self.userName = pickle.load(i)
        return True

    def saveEvent(self):
        """
        saves the event using it's local username and id. 
        """
        if not os.path.exists(f'events\{self.userName}'):
            os.makedirs(f'events\{self.userName}')
        with open(f'events\\{self.userName}\\{self.id}.pkl', 'wb') as i:
            pickle.dump([self.start,self.end,self.eventName,self.description,self.location,self.userName],i)
        pass
    def deleteSelf(self,MaxId):
        """
        Deletes self and updates the file names for all the files with a higher ID than it
        ---
        parameters:
        MaxId: The largest id for this user

        """
        os.remove(f'events\{self.userName}\{self.id}.pkl')
        id = self.id+1
        while os.path.exists(f'events\{self.userName}\{id}.pkl'):
            os.rename(f'events\{self.username}\{id}.pkl',f'events\{self.username}\{id-1}.pkl')
            id+=1