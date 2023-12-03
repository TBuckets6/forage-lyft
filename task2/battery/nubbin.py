# flake8: noqa

from battery import Battery
from datetime import datetime

class Nubbin(Battery):
    
    def __init__(self, current_date: datetime, last_service_date: datetime):
        #converts string such as 'Nov 30 2023' to datetime object
        self.current_date = datetime.strptime(current_date, '%b %d %Y')
        self.last_service_date = datetime.strptime(last_service_date, '%b %d %Y')
    
    def needs_service(self) -> bool:
        #gets the difference in days between current_date and last_service_date
        deltaDays = (self.current_date - self.last_service_date).days
        #if the battery hasnt been changed in 4 years, then return true
        return deltaDays >= 1460
        
#Tests
# nub1 = Nubbin('Nov 30 2023', 'Jun 2 2016')
# nub2 = Nubbin('Nov 30 2023', 'Jun 2 2020')
# print(nub1.needs_service())
# print(nub2.needs_service())
