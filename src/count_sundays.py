import datetime
import calendar

def countSundays(self):
    theDate = datetime.date(1901,1,1)
    maxDate = datetime.date(2000,12,31)
    numberOfSundays = 0
    
    while theDate < maxDate:
        if theDate.weekday() == 6:
            numberOfSundays = numberOfSundays + 1
    
        theDate = add_months(theDate, 1)
    return numberOfSundays

def add_months(sourcedate,months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month / 12
    month = month % 12 + 1
    day = min(sourcedate.day,calendar.monthrange(year,month)[1])
    return datetime.date(year,month,day)

if __name__ == '__main__':
    print countSundays(None)