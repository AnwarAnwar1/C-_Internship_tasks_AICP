# Define arrays for item code, description, and price
case_items = {"A1": "Compact", "A2": "Tower"}
case_prices = {"A1": 75.00, "A2": 150.00}

ram_items = {"B1": "8 GB", "B2": "16 GB", "B3": "32 GB"}
ram_prices = {"B1": 79.99, "B2": 149.99, "B3": 299.99}

hdd_items = {"C1": "1 TB HDD", "C2": "2 TB HDD", "C3": "4 TB HDD"}
hdd_prices = {"C1": 49.99, "C2": 89.99, "C3": 129.99}

# Function to display menu and get user's choice
def display_menu(items, prices, category):
    print(f"\n{category} Options:")
    for code, description in items.items():
        print(f"{code}: {description} - ${prices[code]:.2f}")

    while True:
        user_choice = input(f"Choose {category} (Enter item code): ").upper()
        if user_choice in items:
            return user_choice
        else:
            print("Invalid choice. Please enter a valid item code.")

# Function to calculate the total price of the computer
def calculate_total_price(case, ram, hdd):
    basic_components_price = 200.00
    total_price = basic_components_price + case_prices[case] + ram_prices[ram] + hdd_prices[hdd]
    return total_price

# Main program
print("Welcome to the Online Computer Shop!")

# Get user's choices for case, RAM, and HDD
chosen_case = display_menu(case_items, case_prices, "Case")
chosen_ram = display_menu(ram_items, ram_prices, "RAM")
chosen_hdd = display_menu(hdd_items, hdd_prices, "Main Hard Disk Drive")

# Calculate the total price
total_price = calculate_total_price(chosen_case, chosen_ram, chosen_hdd)

# Display the chosen items and total price
print("\nChosen Items:")
print(f"Case: {chosen_case} - {case_items[chosen_case]}")
print(f"RAM: {chosen_ram} - {ram_items[chosen_ram]}")
print(f"Main Hard Disk Drive: {chosen_hdd} - {hdd_items[chosen_hdd]}")
print(f"Total Price: ${total_price:.2f}")
