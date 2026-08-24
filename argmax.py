import numpy as np

products = np.array([
    "Laptop", "Mouse", "Keyboard", "Monitor",
    "Headphones", "Webcam", "USB Cable"
])

price = np.array([
    55000, 700, 1500, 12000,
    2500, 1800, 400
])

index = np.argmax(price)

print("Most Expensive:", products[index])