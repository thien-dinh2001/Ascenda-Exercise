from abc import ABC, abstractmethod

class IOfferSelector(ABC):
    @abstractmethod
    def select_offer(self, offer, first, second):
        pass