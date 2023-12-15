from abc import ABC, abstractmethod

class ICategoryValidation(ABC):
    
    @abstractmethod
    def validate_category(self, offer):
        pass