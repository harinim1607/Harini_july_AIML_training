# Part A - Bug demonstration

def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))

print("\nCorrect Version:")

# Part B - Fixed version

def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart

print(add_item_fixed("apple"))
print(add_item_fixed("banana"))

# Part C - Shopping Cart

def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }

def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({
        "name": name,
        "price": price,
        "qty": qty
    })

def update_price(price_tuple, new_price):
    # Tuples are immutable.
    # Trying to change them raises a TypeError.
    pass

def calculate_total(cart):
    total = 0

    for item in cart["items"]:
        total += item["price"] * item["qty"]

    total = total - (total * cart["discount"] / 100)
    return total

cart1 = create_cart("Harini", 10)
cart2 = create_cart("Aarav")

add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 500, 2)

add_to_cart(cart2, "Book", 400, 3)

print("\nCustomer 1 Total:", calculate_total(cart1))
print("Customer 2 Total:", calculate_total(cart2))

# Discussion:
# discount=0 is safe because integers are immutable.
# cart=[] is dangerous because lists are mutable and shared.
# Rebinding means assigning a new object.
# Mutating means changing the existing object.
# Mutable: list, dict, set
# Immutable: tuple, str, int
# Lists passed into functions are modified outside because they are mutable.