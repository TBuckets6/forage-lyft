# flake8: noqa

from abc import ABC

class Battery(ABC):
    def needs_service(self):
        pass