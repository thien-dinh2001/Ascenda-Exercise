from abc import ABC, abstractmethod
import datetime

from model.offer import Offer

class IDateValidation(ABC):
    @abstractmethod
    def validate_date(self, checkin_date: datetime, offer: Offer):
        pass