# add.py
# Handles adding new medicines to inventory

from inventory import save_inventory

def add_medicine(inventory):
    print("\n--- Add New Medicine ---")
    name = input("Enter medicine name: ").strip()
    brand = input("Enter brand name: ").strip()
    if not name or not brand:
        print("Name and brand cannot be empty!")
        return

    # Check duplicates
    for item in inventory:
        if item["name"].lower() == name.lower() and item["brand"].lower() == brand.lower():
            print("Medicine already exists!")
            return

    try:
        qty = int(input("Enter initial quantity (tablets): "))
        rate_tab = int(input("Enter rate per tablet: "))
        rate_strip = int(input("Enter rate per strip: "))
        tabs_per_strip = int(input("Enter tablets per strip: "))
    except ValueError:
        print("Invalid input! Enter numbers only.")
        return

    if qty < 0 or rate_tab < 0 or rate_strip < 0 or tabs_per_strip <= 0:
        print("Values must be positive!")
        return

    new_item = {
        "name": name,
        "brand": brand,
        "qty": qty,
        "rate_tab": rate_tab,
        "rate_strip": rate_strip,
        "tabs_per_strip": tabs_per_strip
    }

    try:
        inventory.append(new_item)
        save_inventory(inventory)
    except Exception as e:
        print(f"Error saving inventory: {e}")
        return

    print(f"{name} ({brand}) added successfully!")