from abc import ABC, abstractmethod

class IInputHandler(ABC):
    @abstractmethod
    def read(self):
        pass