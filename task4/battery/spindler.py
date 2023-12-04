# flake8: noqa

from battery.battery import Battery
from datetime import datetime

class Spindler(Battery):
    
    def __init__(self, current_date: datetime, last_service_date: datetime):
        #converts string such as 'Nov 30 2023' to datetime object
        self.current_date = datetime.strptime(current_date, '%b %d %Y')
        self.last_service_date = datetime.strptime(last_service_date, '%b %d %Y')
    
    def needs_service(self) -> bool:
        #gets the difference in days between current_date and last_service_date
        deltaDays = (self.current_date - self.last_service_date).days
        #if the battery hasnt been changed in 2 years, then return true
        return deltaDays >= 1095 # 3 years
        
#Tests
# spin1 = Spindler('Nov 30 2023', 'Jun 2 2016')
# spin2 = Spindler('Nov 30 2023', 'Jun 2 2020')
# print(spin1.needs_service())
# print(spin2.needs_service())