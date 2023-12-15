from handler.interfaces.category_validation_interface import ICategoryValidation

class CategoryValidation(ICategoryValidation):
    
    def __init__(self, valid_category) -> None:
        self.valid_category = valid_category

    def validate_category(self, offer):
        if offer.category in self.valid_category:
            return True
        else:
            return False