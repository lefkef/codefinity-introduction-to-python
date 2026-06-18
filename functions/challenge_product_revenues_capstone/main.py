# Task 1: Define a function to calculate the revenue for each product
def calculate_revenue(prices, quantities_sold):
    revenue = []
    for index in range(len(prices)):
        revenue.append(prices[index] * quantities_sold[index])
    return revenue

# Task 2: Define a function to format and display the sorted revenues
def formatted_output(revenues):
    for product, rev in sorted(revenues):
        print(f"{product} has total revenue of ${rev}")

# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

# Task 3: Call the `calculate_revenue()` function to get total `revenue` for each product
revenue = calculate_revenue(prices, quantities_sold)

# Task 4: Use `zip()` to combine the products and their corresponding revenues into a list
revenue_per_product = list(zip(products, revenue))

# Task 5: Display the sorted revenues using the `formatted_output()` function
formatted_output(revenue_per_product)