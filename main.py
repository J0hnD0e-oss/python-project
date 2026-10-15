# main.py
# The main program for MEDSTORE system.
# - Provides menu interface to display, sell, restock, and add medicines
# - Uses modules: inventory.py, sales.py, restock.py, add.py

from inventory import load_inventory, display_inventory
from sales import sell_medicine
from restock import restock_medicine
from add import add_medicine

def main():
    inventory = load_inventory()  # Load inventory from file at start

    while True:
        # Display menu
        print("\n--- MEDSTORE SYSTEM ---")
        print("1. Display Medicines")
        print("2. Sell Medicines")
        print("3. Restock Medicines")
        print("4. Add New Medicine")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        # Handle menu selection
        if choice == "1":
            display_inventory(inventory)
        elif choice == "2":
            sell_medicine(inventory)
        elif choice == "3":
            restock_medicine(inventory)
        elif choice == "4":
            add_medicine(inventory)
        elif choice == "5":
            print("Exiting")
            break
        else:
            print("Invalid choice! Enter a number 1-5.")

if __name__ == "__main__":
    main()