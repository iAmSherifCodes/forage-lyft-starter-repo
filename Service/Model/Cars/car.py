import abc
from abc import ABC

from Service.Model.Batteries.Battery import Battery
from Service.Model.Engines.Engine import Engine
from Service.Model.Serviceable import Serviceable


class Car(Serviceable, ABC):

    def __init__(self, engine: Engine, battery: Battery):
        self._engine: Engine = engine
        self._battery: Battery = battery

    @abc.abstractmethod
    def needs_service(self) -> bool:
        pass
