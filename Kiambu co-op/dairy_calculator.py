"""Kiambu Dairy Co-op Payment Calculator.

Reads a local price file to calculate exact farmer payout figures cleanly.
"""


def get_current_price():
    """Reads current milk price from configuration file, falling back to default."""
    try:
        with open("price.txt", "r") as f:
            return float(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 55.0  # Fallback standard rate per litre


def calculate_payment(litres, price_per_litre):
    """Computes total financial amount owed to farmer."""
    return litres * price_per_litre


def run():
    print("======================================")
    print(" Kiambu Dairy Co-op Payment Calculator")
    print("======================================")
    current_price = get_current_price()
    print(f"Active Buying Price: KES {current_price:.2f} per litre\n")

    name = input("Enter Farmer Name: ").strip()
    if not name:
        print("❌ Error: Farmer name cannot be left blank.")
        return

    try:
        litres = float(input("Enter Litres Supplied: "))
        if litres <= 0:
            print("❌ Error: Litres supplied must be greater than zero.")
            return
    except ValueError:
        print("❌ Error: Invalid input. Please enter a valid number.")
        return

    total_owed = calculate_payment(litres, current_price)

    print("\n--------------------------------------")
    print(f"Farmer Statement Summary")
    print("--------------------------------------")
    print(f"Farmer Name : {name}")
    print(f"Supply Vol. : {litres:.2f} Litres")
    print(f"Rate Applied: KES {current_price:.2f}/Litre")
    print(f"Total Owed  : KES {total_owed:,.2f}")
    print("--------------------------------------")


if __name__ == "__main__":
    run()
