import re

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

    # Dictionary to count the occurences of each SKU
    item_count = {}

    # Regex for matching the sigle and multiple quantities (e.g B, or 3A)
    # Assumed all products use capital skus
    pattern = re.compile(r'(\d+)([A-Z])|([A-Z])|(.+)')

    #Find all matches
    matches = pattern.findall(skus)

    for match in matches:
        if match[3]:  #unvalid group
            return -1
        elif match[2]: # single letters cases, like "A"
            sku = match[2]
            quantity = 1
        else: # number letter cases, like "3B"
            quantity = int(match[0])
            sku = match[1]
        
        if  sku not in prices:
            return -1
        
        item_count[sku] = item_count.get(sku, 0) + quantity
    
    # Calculate total price
    total_price = 0
    for item, count in item_count.items():
        if item in offers:
            offer_quantity, offer_price = offers[item]
            total_price += (count // offer_quantity) * offer_price
            total_price += (count % offer_quantity) * prices[item]
        else:
            total_price += count * prices[item]
    
    return total_price
    




