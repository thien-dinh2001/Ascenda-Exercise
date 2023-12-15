from datetime import *
from handler.interfaces.date_validation_interface import IDateValidation

from model.offer import Offer
class DateValidation(IDateValidation):
    def __init__(self, time_interval) -> None:
        self.min_time_interval = time_interval

    def validate_date(self, checkin_date: datetime, offer: Offer):
        if offer.valid_to >= checkin_date + timedelta(days=self.min_time_interval):
            return True
        else:
            return False