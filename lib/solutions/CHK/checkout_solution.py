import re
from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    """The checkout function calculates the total price of items in a supermarket basket based on
    the provided input string. The string can contain Stock Keeping Units (SKUs), each identified
    by a letter (e.g., A, B, C, etc.), and optionally prefixed by a number indicating the quantity
    of that item. If a number is not specified before a letter, a quantity of one is assumed."""

    # Price tables
    prices = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10,
        'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 70, 'L': 90,
        'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
        'S': 20, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 17,
        'Y': 20, 'Z': 21
    }
    
    # Special offers
    offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'H': [(10, 80), (5, 45)],
        'K': [(2, 120)],
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'V': [(3, 130), (2, 90)],
    }

    # Free items offer
    free_items = {
        'E': ('B', 2),   # Buy 2E, get 1B free
        'F': ('F', 3),   # Buy 3F, pay for 2F (essentially buy 2, get 1 free)
        'N': ('M', 3),   # Buy 3N, get 1M free
        'R': ('Q', 3),   # Buy 3R, get 1Q free
        'U': ('U', 4)    # Buy 4U, pay for 3U (essentially buy 3, get 1 free)
    }

    # Group discount offer (buy any 3 of S, T, X, Y, Z for 45)
    group_discount = {
        'group': ['S', 'T', 'X', 'Y', 'Z'],
        'count': 3,
        'price': 45
    }

    # Dictionary to count the occurences of each SKU
    item_count = defaultdict(int)

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
    
    # Apply group discount offer, prioritizing the cheapest items first
    group_items = [sku for sku in group_discount['group'] if item_count[sku] > 0]
    group_items.sort(key=lambda x: -prices[x])  # Sort by price ascending

    group_count = sum(item_count[sku] for sku in group_items)
    total_price = 0

    while group_count >= group_discount['count']:
        total_price += group_discount['price']
        group_count -= group_discount['count']

        # Reduce the count of the cheapest items first
        count_of_items = group_discount['count']
        for sku in group_items:
            if item_count[sku] >= count_of_items:
                item_count[sku] -= count_of_items
                break
            else:
                count_of_items -= item_count[sku]
                item_count[sku] = 0

    # Apply offers that give free items
    for sku, (free_sku, required_quantity) in free_items.items():
        if sku in item_count and free_sku in item_count:
            free_count = item_count[sku] // required_quantity
            item_count[free_sku] = max(0, item_count[free_sku] - free_count)
    

    
    # Calculate total price
    for item, count in item_count.items():
        print(f"total price is: {total_price}, item is: {item} and count is: {count}")
        if item in offers:
            print('hi')
            # Apply special offers for the item
            item_offers = sorted(offers[item], key=lambda x: -x[0])  # Sort offers by quantity descending
            for offer_quantity, offer_price in item_offers:
                if count >= offer_quantity:
                    total_price += (count // offer_quantity) * offer_price
                    count %= offer_quantity
            total_price += count * prices[item]
        else:
            total_price += count * prices[item]

    print("-------")
    
    return total_price
    






