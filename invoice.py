# invoice.py
# Generates sales and restock invoices in table format

from datetime import datetime

COUNTER_FILE = "invoice_counter.txt"

def get_next_invoice_number():
    """Get the next invoice number and update counter."""
    try:
        with open(COUNTER_FILE, "r") as file:
            number = int(file.read())
    except (FileNotFoundError, ValueError):
        number = 1

    try:
        with open(COUNTER_FILE, "w") as file:
            file.write(str(number + 1))
    except Exception as e:
        print(f"Error updating invoice counter: {e}")
    return number

def generate_filename(prefix):
    """Generate a unique filename for the invoice."""
    number = get_next_invoice_number()
    return f"{prefix}_INV{number:03}.txt"

def generate_sales_invoice(customer, cart, total_amount):
    """Generate a sales invoice in table format."""
    filename = generate_filename("sales_invoice")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(filename, "w") as file:
            file.write("MEDSTORE SALES INVOICE\n")
            file.write(f"Customer: {customer}\n")
            file.write(f"Date: {date}\n\n")
            file.write(f"{'Name':<20} {'Brand':<20} {'Unit':<8} {'Qty':<5} {'Discount':<10} {'Cost':<10}\n")
            file.write("-" * 80 + "\n")
            for item, unit, qty, discount, cost in cart:
                file.write(f"{item['name']:<20} {item['brand']:<20} {unit:<8} {qty:<5} {discount:<10.2f} {cost:<10.2f}\n")
            file.write("-" * 80 + "\n")
            file.write(f"{'TOTAL':>63} {total_amount:<10.2f}\n")
        print(f"Invoice generated: {filename}")
    except Exception as e:
        print(f"Error generating invoice: {e}")

def generate_restock_invoice(supplier, cart, total_amount):
    """Generate a restock invoice in table format."""
    filename = generate_filename("restock_invoice")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(filename, "w") as file:
            file.write("MEDSTORE RESTOCK INVOICE\n")
            file.write(f"Supplier: {supplier}\n")
            file.write(f"Date: {date}\n\n")
            file.write(f"{'Name':<20} {'Brand':<20} {'Unit':<8} {'Qty':<5} {'Cost':<10}\n")
            file.write("-" * 70 + "\n")
            for item, unit, qty, cost in cart:
                file.write(f"{item['name']:<20} {item['brand']:<20} {unit:<8} {qty:<5} {cost:<10.2f}\n")
            file.write("-" * 70 + "\n")
            file.write(f"{'TOTAL':>53} {total_amount:<10.2f}\n")
        print(f"Restock invoice generated: {filename}")
    except Exception as e:
        print(f"Error generating restock invoice: {e}")