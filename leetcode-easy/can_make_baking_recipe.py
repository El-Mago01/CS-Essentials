"""
Write a function can_make_recipe(available, recipe) that takes two dictionaries:
available: A dictionary of ingredients you have at home with their available quantities.
recipe: A dictionary of ingredients required for the recipe along with the quantities needed.
The function should return True if every ingredient in the recipe is available in sufficient quantity
(i.e., the available quantity is equal to or greater than the required quantity). Otherwise, return False.
"""

def can_make_recipe(available_goods, needed):
    for required_item, required_amount in needed.items():
        print(f"...checking : {required_item}. Must have {required_amount} : ", end="")
        if required_item in available_goods:
            available_amount = available_goods[required_item]
            if available_amount < required_amount:
                print(f"ONLY {available_amount} AVAILABLE. BUY AT LEAST {required_amount-available_amount} MORE")
                return False
            else:
                print(f"OK, {available_amount} is/are available.")
        else:
            print(f"ITEM NOT AVAILABLE. BUY AT LEAST {required_amount}")
            return False
    return True

# Available ingredients:
available = {
    "flour": 500,    # grams
    "sugar": 200,    # grams
    "eggs": 4,       # count
    "milk": 300      # milliliters
}

# Recipe requirements:
recipe = {
    "flour": 300,    # grams
    "sugar": 100,    # grams
    "eggs": 2,        # count
    "cheese" : 2       # slices
}
print("The statement:")
print(f"With the ingredients available, I can make the recipe is : {can_make_recipe(available, recipe)}")
# Expected output: True, because there is enough of every ingredient.