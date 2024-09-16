

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    """The checkout function calculates the total price of items in a supermarket basket based on
    the provided input string. The string can contain Stock Keeping Units (SKUs), each identified
    by a letter (e.g., A, B, C, etc.), and optionally prefixed by a number indicating the quantity
    of that item. If a number is not specified before a letter, a quantity of one is assumed."""

    # Price tables
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }

   # Special offers
    offers = {
       'A': (3, 130),
       'B': (2, 45)
    }
    


