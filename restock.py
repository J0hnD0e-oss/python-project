# restock.py
# Handles restocking medicines, updating inventory, and generating restock invoices

from inventory import display_inventory, save_inventory
from invoice import generate_restock_invoice

def restock_medicine(inventory):
    """
    Restock medicines from supplier.
    - Displays inventory
    - Allows selection of medicines and quantity
    - Calculates total cost for buyer
    - Updates inventory and generates restock invoice
    """
    display_inventory(inventory)
    supplier = input("Enter supplier name: ").strip()
    if not supplier:
        print("Supplier name cannot be empty!")
        return

    cart = []  # Stores items restocked
    total_amount = 0

    while True:
        # Select medicine
        try:
            choice = int(input("Select medicine number to restock (0 to finish): "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if choice == 0:
            break
        if choice < 1 or choice > len(inventory):
            print("Invalid selection!")
            continue

        item = inventory[choice - 1]

        # Select unit
        unit = input("Unit (tablet/strip): ").lower()
        if unit not in ["tablet", "strip"]:
            print("Invalid unit! Must be 'tablet' or 'strip'.")
            continue

        # Enter quantity
        try:
            qty = int(input("Enter quantity to restock: "))
        except ValueError:
            print("Invalid quantity!")
            continue
        if qty <= 0:
            print("Quantity must be positive!")
            continue

        # Calculate number of tablets added and cost
        if unit == "tablet":
            tablets_added = qty
            cost = qty * item["rate_tab"]
        else:  # strip
            tablets_added = qty * item["tabs_per_strip"]
            cost = qty * item["rate_strip"]

        # Update inventory
        item["qty"] += tablets_added

        # Add to restock cart
        cart.append((item, unit, qty, cost))
        total_amount += cost

    # Display restock invoice in console
    if cart:
        print("\nRESTOCK INVOICE")
        print(f"{'Name':<20} {'Brand':<20} {'Unit':<8} {'Qty':<5} {'Cost':<10}")
        print("-" * 70)
        for item, unit, qty, cost in cart:
            print(f"{item['name']:<20} {item['brand']:<20} {unit:<8} {qty:<5} {cost:<10.2f}")
        print("-" * 70)
        print(f"{'TOTAL':>53} {total_amount:<10.2f}")

    # Save inventory and generate text invoice
    try:
        save_inventory(inventory)
        generate_restock_invoice(supplier, cart, total_amount)
    except Exception as e:
        print(f"Error saving inventory or generating invoice: {e}")