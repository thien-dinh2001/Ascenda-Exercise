import json
from typing import Type

class Merchant:
    def __init__(self, data: json) -> None:
        self.id = data['id']
        self.name = data['name']
        self.distance = data['distance']
    
    def __lt__(self, other: Type['Merchant']) -> bool:
        return self.distance < other.distance
    
    def to_dict(self) -> json:
        return self.__dict__
