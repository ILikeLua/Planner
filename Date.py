class Date:
    Day = 0
    Month = 0
    Year = 0
    def __init__(self, Day, Month, Year) -> None:
        if Month > 12:
            Month = 12
        if Month < 1:
            Month = 1
        if Day < 1:
            Day = 1
        elif Year % 4 == 0 and Month == 2:
            if Day > 28:
                Day = 28
        elif Month == 2:
            if Day > 29:
                Day = 29
        elif Month in [1,3,5,7,8,10,12]:
            if Day > 31:
                Day = 31
        elif Month in [4,6,9,11]:
            if Day > 30:
                Day = 30
        self.Day = Day
        self.Month = Month
        self.Year = Year
        pass
    def __str__(self):
        return f'{"" if self.Month > 9 else "0"}{self.Month}/{"" if self.Day > 9 else "0"}{self.Day}/{self.Year}'
class Time:
    Minute = 0
    Hour = 0
    def __init__(self, Minute, Hour) -> None:
        self.Minute =  0 if Minute < 0 else 59 if Minute > 59 else Minute
        self.Hour = 0 if Hour < 0 else 23 if Hour > 23 else Hour
        pass
    def __str__(self):
        return f'{"" if (self.Hour%12)+1 > 9 else "0"}{(self.Hour%12)+1}:{"" if self.Minute > 9 else "0"}{self.Minute} {"PM" if self.Hour > 11 else "AM"}'
class DateTime:
    def __init__(self, time: Time , date: Date) -> None:
        self.time = time  
        self.date = date
    def __str__(self) -> str:
        return f'{self.date}\n{self.time}'