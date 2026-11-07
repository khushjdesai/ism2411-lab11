# ==========================================
# REFLECTION QUESTIONS
# 1. In Exercise 3 you saw the difference between .get() and bracket notation. When in real work would you use each one, and what's your rule of thumb for choosing?
#    - Use .get() when a key might occasionally be missing (such as optional profile fields) to prevent the program from crashing. 
#      Use bracket notation when a key is strictly required, ensuring your code fails fast if critical data is missing. 
#      Rule of thumb: use .get() for external, optional, or unpredictable data, and brackets for guaranteed core keys.
# 2. Exercise 8 asked you to build a summary dictionary with a loop. What does this pattern remind you of from Excel, and why might the Python version be more useful for large datasets?
#    - This pattern is very similar to an Excel Pivot Table or a SUMIF/SUMIFS formula aggregating data by a specific category. 
#      Python is more useful for massive datasets because it processes millions of records in seconds without spreadsheet lagging, formula corruption, or crashing.
# ==========================================

# --- EXERCISE 1: One customer ---
print("--- Exercise 1 ---")
customer = {
    "name": "Alice Smith",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50
}
print("Name:", customer["name"])
print("Email:", customer["email"])
print("Tier:", customer["tier"])
print("YTD Spend:", customer["ytd_spend"])
print("Full dict:", customer)


# --- EXERCISE 2: Update and add ---
print("\n--- Exercise 2 ---")
customer["phone"] = "555-0199"
print("After adding phone:", customer)

customer["tier"] = "platinum"
print("After updating tier:", customer)

del customer["email"]
print("After deleting email:", customer)


# --- EXERCISE 3: Safe lookup ---
print("\n--- Exercise 3 ---")
# Using .get() to look up the deleted email safely
email_lookup = customer.get("email", "no email on file")
print("Safe lookup (.get):", email_lookup)

# Using bracket notation which raises a KeyError (caught via try/except)
try:
    print(customer["email"])
except KeyError:
    print("KeyError caught: 'email' key no longer exists in the dictionary.")


# --- EXERCISE 4: Iterate ---
print("\n--- Exercise 4 ---")
for key, value in customer.items():
    print(f"{key}: {value}")

# Note on iterating without .items():
# If you loop through a dictionary without calling .items() (e.g., `for key in customer:`), 
# Python only iterates over the keys themselves, meaning you would have to manually look up each value using bracket notation.


# --- EXERCISE 5: Lookup table ---
print("\n--- Exercise 5 ---")
tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.10, "platinum": 0.15}
current_tier = customer["tier"]
discount_rate = tier_discounts.get(current_tier, 0)

purchase_amount = 200
final_price = purchase_amount * (1 - discount_rate)

print(f"Tier: {current_tier} · Discount Rate: {discount_rate * 100}% · Final Price: ${final_price:.2f}")


# --- EXERCISE 6: List of dicts ---
print("\n--- Exercise 6 ---")
customer1 = {"name": "Alice", "tier": "platinum"}
customer2 = {"name": "Bob", "tier": "silver"}
customer3 = {"name": "Charlie", "tier": "bronze"}
customers_list = [customer1, customer2, customer3]

spend_amount = 300
for c in customers_list:
    t = c["tier"]
    rate = tier_discounts.get(t, 0)
    discount_amount = spend_amount * rate
    print(f"Name: {c['name']}, Tier: {t}, Discount on $300: ${discount_amount:.2f}")


# --- EXERCISE 7: Nested catalog ---
print("\n--- Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK ALERT: {product} has only {details['stock']} items left!")


# --- EXERCISE 8: Sales by region ---
print("\n--- Exercise 8 ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

region_summary = {}
for tx in transactions:
    reg = tx["region"]
    amt = tx["amount"]
    region_summary[reg] = region_summary.get(reg, 0) + amt

# Print final summary sorted by region name alphabetically
sorted_summary = sorted(region_summary.items())
for reg, total in sorted_summary:
    print(f"{reg}: {total}")