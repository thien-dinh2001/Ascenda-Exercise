from typing import *
from output.output_interface import IOutputHandler
from model.offer import Offer
import json
from model.merchant import Merchant
from datetime import *

class OutputHandler(IOutputHandler):
    def __init__(self, path) -> None:
        self.path = path

    def write(self, selected_offers: List[Offer]):
        serialized_offers = []

        if None not in selected_offers:
            if selected_offers[0].id > selected_offers[1].id:
                t = selected_offers[0]
                selected_offers[0] = selected_offers[1]
                selected_offers[1] = t  

        for offer in selected_offers:
            if offer is not None:
                serialized_offers.append(offer.to_dict())
                
        formatted_data = {"offers": serialized_offers}   
        with open(self.path, 'w') as json_file:
            json.dump(formatted_data, json_file, default= self._serialize, indent=2)


    def _serialize(self, obj):
            if isinstance(obj, datetime):
                return obj.strftime("%Y-%m-%d")
            elif isinstance(obj, Merchant):
                return obj.__dict__
            else:
                raise TypeError(f"Object of type {type(obj)} is not JSON serializable")