# flake8: noqa

from abc import ABC

class Engine(ABC):
    def needs_service(self):
        pass