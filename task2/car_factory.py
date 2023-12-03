# flake8: noqa

from car import Car

from battery.nubbin import Nubbin
from battery.spindler import Spindler

from engine.capulet import Capulet
from engine.sternman import Sternman
from engine.willoughby import Willoughby

class CarFactory:
    
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Capulet(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        car = Car(engine,battery)
        return car
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Willoughby(last_service_mileage, current_mileage)
        battery = Spindler(current_date, last_service_date)
        car = Car(engine,battery)
        return car
    
    def create_palindrome(current_date, last_service_date, warning_light_on):
        engine = Sternman(warning_light_on)
        battery = Spindler(current_date, last_service_date)
        car = Car(engine, battery)
        return car
    
    def create_rorscach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Willoughby(last_service_mileage, current_mileage)
        battery = Nubbin(current_date, last_service_date)
        car = Car(engine, battery)
        return car
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = Capulet(last_service_mileage, current_mileage)
        battery = Nubbin(current_date, last_service_date)
        car = Car(engine, battery)
        return car