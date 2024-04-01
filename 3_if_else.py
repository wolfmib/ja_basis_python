# Code to compare sales profits using if-else statements
import random

# Generate sales data
sales_data = [(f"Sale_{i}", random.randint(4000, 7000)) for i in range(1, 6)]

# Filter sales with profits > 5000
high_profit_sales = [(name, profit) for name, profit in sales_data if profit > 5000]

if high_profit_sales:
    highest_sale = max(high_profit_sales, key=lambda x: x[1])
    print(f"The sale with the highest profit is: {highest_sale[0]}")
    print(f"Profit: {highest_sale[1]}")
else:
    print("No sales with profits greater than 5000.")


print("Total data")
print(sales_data)
