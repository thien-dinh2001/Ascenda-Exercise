from typing import *
from model.offer import Offer
from abc import ABC, abstractmethod

class IOutputHandler(ABC):
    @abstractmethod
    def write(self, selected_offers: List[Offer]):
        pass