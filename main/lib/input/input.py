import json
from lib.input.input_interface import IInputHandler
from model.offer import Offer

class InputHandler(IInputHandler):
    def __init__(self, path) -> None:
        self.path = path
    def read(self):
        with open(self.path, 'r') as file:
            offers = json.load(file)['offers']
            for offer in offers:
                yield Offer(offer)
    
