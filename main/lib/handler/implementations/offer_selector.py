from handler.interfaces.offer_selector_interface import IOfferSelector

class OfferSelector(IOfferSelector):
    
    def select_offer(self, offer, first, second):
        if first is None:
            first = offer
        elif offer < first:
            if offer.category == first.category:
                first = offer
            else:
                second = first
                first = offer
        elif offer.category != first.category:
            if second is None or offer < second:
                second = offer
        return [first, second]