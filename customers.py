# Self Assessment Questions
# 1. I would use .get() if I'm not sure if a key is in a dictionairy, and I would use the bracket notation if I know a key is there. I would use .get() so there isn't any errors if there's no key.
# 2. This pattern reminds me of adding up sales in Excel. Python is better for more data because it calculates faster, saving time for someone.

# Exercise 1
customer = {
    "name": "Chase",
    "email": "chase@gmail.com",
    "tier": "gold",
    "ytd_spend": 1500
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# Exercise 2
customer["phone"] = "941-518-0851"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)

# Exercise 3
print(customer.get("email", "no email on file"))
try:
    print(customer["email"])
except KeyError:
    print("Email not found")

# Exercise 4
for key, value in customer.items():
    print(f"{key}: {value}")
for key in customer:
    print(key)
# Using .items() gives the key and its value. When not using .items(), the loop only gives the keys. 

# Exercise 5
tier_discounts = {"bronze": 0, "silver": .05, "gold": .1, "platinum": .15}
tier = customer["tier"]
discount = tier_discounts.get(tier,0)
price = 200
final_price = price * (1 - discount)
print(f"Tier: {tier}")
print(f"Discount: {discount * 100}%")
print(f"Final price: ${final_price:.2f}")

# Exercie 6
customers = [
    {"name": "Chase", "tier": "platinum"},
    {"name": "Josh", "tier": "gold"},
    {"name": "Eduardo", "tier": "silver"}
]

for person in customers:
    name = person["name"]
    tier = person["tier"]
    discount = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount
    print(f"{name} - {tier} - Discount: ${discount_amount:.2f}")

# Exercise 7
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product}")

# Exercise 8
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

summary = {}
for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    summary[region] = summary.get(region, 0) + amount
for region in sorted(summary):
    print(f"{region}: {summary[region]}")
