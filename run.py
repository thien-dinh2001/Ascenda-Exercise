import sys

for path in ['./main/', './main/lib/', './main/model/', './main/constants/', './main/lib/handler/']:
    sys.path.append(path)

from constants import *
from implementations.category_validation import CategoryValidation
from implementations.date_validation import DateValidation
from input.input import InputHandler
from output.output import OutputHandler
from implementations.offer_selector import OfferSelector
from datetime import *


def main(checkin_date):
    input_handler = InputHandler(INPUT_PATH_FILE)
    output_handler = OutputHandler(OUTPUT_PATH_FILE)
    date_filter = DateValidation(MIN_TIME_INTERVAL)
    category_filter = CategoryValidation(VALID_CATEGORY)
    selector = OfferSelector()

    try: 
        checkin = datetime.strptime(checkin_date, '''%Y-%m-%d''') 
    except ValueError:
        print(f"Error: The provided date '{checkin_date}' is not in the expected format (YYYY-MM-DD).")
        sys.exit(1)
    
    gen = input_handler.read()
    selected_offers = [None, None]
    offer = next(gen, None)
    while offer is not None:
        if date_filter.validate_date(checkin, offer) and category_filter.validate_category(offer): 
            selected_offers = selector.select_offer(offer, selected_offers[0], selected_offers[1])
        offer = next(gen, None)
    output_handler.write(selected_offers)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python run.py <checkin_date>")
        sys.exit(1)

    checkin_date = sys.argv[1]
    main(checkin_date)
