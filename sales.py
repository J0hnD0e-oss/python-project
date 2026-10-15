# sales.py
# Handles selling medicines to customers with table output and updates inventory

from inventory import display_inventory, save_inventory
from invoice import generate_sales_invoice

def sell_medicine(inventory):
    """
    Sell medicines to customers.
    - Displays inventory
    - Allows selection of medicines and quantity
    - Calculates cost and discounts
    - Updates inventory and generates sales invoice
    """
    display_inventory(inventory)
    customer = input("Enter customer name: ").strip()
    if not customer:
        print("Customer name cannot be empty!")
        return

    cart = []  # Stores items purchased in this transaction
    total_amount = 0

    while True:
        # Get medicine selection
        try:
            choice = int(input("Select medicine number (0 to finish): "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if choice == 0:
            break
        if choice < 1 or choice > len(inventory):
            print("Invalid selection!")
            continue

        item = inventory[choice - 1]
        unit = input("Unit (tablet/strip): ").lower()

        # Get quantity
        try:
            qty = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid quantity!")
            continue
        if qty <= 0:
            print("Quantity must be positive!")
            continue

        # Calculate cost and check stock
        if unit == "tablet":
            if qty > item["qty"]:
                print("Not enough stock!")
                continue
            cost = qty * item["rate_tab"]
            discount = 0
            item["qty"] -= qty
        elif unit == "strip":
            tablets_needed = qty * item["tabs_per_strip"]
            if tablets_needed > item["qty"]:
                print("Not enough stock!")
                continue
            cost = qty * item["rate_strip"]
            discount = 0
            if qty >= 2:  # Discount for buying 2 or more strips
                discount = cost * 0.05
                cost -= discount
            item["qty"] -= tablets_needed
        else:
            print("Invalid unit!")
            continue

        # Add to cart and update total
        cart.append((item, unit, qty, discount, cost))
        total_amount += cost

    # Print sales invoice in console (table format)
    if cart:
        print("\nSALES INVOICE")
        print(f"{'Name':<20} {'Brand':<20} {'Unit':<8} {'Qty':<5} {'Discount':<10} {'Cost':<10}")
        print("-" * 80)
        for item, unit, qty, discount, cost in cart:
            print(f"{item['name']:<20} {item['brand']:<20} {unit:<8} {qty:<5} {discount:<10.2f} {cost:<10.2f}")
        print("-" * 80)
        print(f"{'TOTAL':>63} {total_amount:<10.2f}")

    # Save inventory and generate text invoice
    try:
        save_inventory(inventory)
        generate_sales_invoice(customer, cart, total_amount)
    except Exception as e:
        print(f"Error saving inventory or generating invoice: {e}")