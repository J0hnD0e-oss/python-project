# inventory.py
# Handles inventory operations: load, save, display in table format

INVENTORY_FILE = "inventory.txt"

def load_inventory():
    """Load inventory from file and return as list of dictionaries."""
    inventory = []
    try:
        with open(INVENTORY_FILE, "r") as file:
            for line in file:
                try:
                    name, brand, qty, rate_tab, rate_strip, tabs_per_strip = line.strip().split(", ")
                    inventory.append({
                        "name": name,
                        "brand": brand,
                        "qty": int(qty),
                        "rate_tab": int(rate_tab),
                        "rate_strip": int(rate_strip),
                        "tabs_per_strip": int(tabs_per_strip)
                    })
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        print("Inventory file not found. Starting empty.")
    except Exception as e:
        print(f"Error loading inventory: {e}")
    return inventory


def save_inventory(inventory):
    """Save inventory to file."""
    try:
        with open(INVENTORY_FILE, "w") as file:
            for item in inventory:
                file.write(
                    f"{item['name']}, {item['brand']}, {item['qty']}, "
                    f"{item['rate_tab']}, {item['rate_strip']}, {item['tabs_per_strip']}\n"
                )
    except Exception as e:
        print(f"Error saving inventory: {e}")


def display_inventory(inventory):
    """Display inventory in a neat table."""
    if not inventory:
        print("\nInventory is empty.")
        return

    print("\nAvailable Medicines:")
    print("-" * 80)
    print(f"{'No.':<4} {'Name':<20} {'Brand':<20} {'Stock':<10} {'Rate/Tab':<10} {'Rate/Strip':<10}")
    print("-" * 80)

    count = 1
    for item in inventory:
        print(
            f"{count:<4} "
            f"{item['name']:<20} "
            f"{item['brand']:<20} "
            f"{item['qty']:<10} "
            f"{item['rate_tab']:<10} "
            f"{item['rate_strip']:<10}"
        )
        count += 1

    print("-" * 80)