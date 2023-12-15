import json
from datetime import datetime
from operator import itemgetter
from functools import reduce
from model.merchant import Merchant
from typing import Any, Type

class Offer:
    def __init__(self, data: json) -> None:
        self.id = int(data['id'])
        self.title = data['title']
        self.description = data['description']
        self.category = data['category']
        self.merchant = reduce(lambda x, y: x if x < y else y, map(Merchant, data['merchants']))
        self.valid_to = datetime.strptime(data['valid_to'], '''%Y-%m-%d''') 

    def __lt__(self, other: Type['Offer']):
        return self.merchant <  other.merchant

    def to_dict(self):
        return self.__dict__
        # return json.dumps(self.__dict__, default= serialize)    
    
    
