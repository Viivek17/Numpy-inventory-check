import numpy as np

# Product data
products = np.array([
    "Laptop", "Mouse", "Keyboard", "Monitor",
    "Headphones", "Webcam", "USB Cable"
])

stock = np.array([5, 45, 12, 3, 8, 20, 50])

price = np.array([55000, 700, 1500, 12000, 2500, 1800, 400])

# Calculate inventory value
values = stock * price

print("=" * 40)
print("Product Information")
print("=" * 40)

for i in range(len(products)):
    print(
        f"{products[i]:12} "
        f"Stock: {stock[i]:3} "
        f"Value: Rs.{values[i]}"
    )

# Total inventory value
total_value = np.sum(values)
print("\nTotal Inventory Value: Rs.", total_value)

# Average stock
average_stock = np.mean(stock)
print("Average Stock:", round(average_stock, 2))

# Most expensive product
max_price = np.argmax(price)
print(
    "Most Expensive:",
    products[max_price],
    "Rs.", price[max_price]
)

# Cheapest product
min_price = np.argmin(price)
print(
    "Cheapest:",
    products[min_price],
    "Rs.", price[min_price]
)

# Low stock products
low_stock = products[stock < 10]

print("\nLow Stock Products")

for product in low_stock:
    print("-", product)

# Highest stock product
high_stock = np.argmax(stock)

print(
    "\nHighest Stock:",
    products[high_stock]
)