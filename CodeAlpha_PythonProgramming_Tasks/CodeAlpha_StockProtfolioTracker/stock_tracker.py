# Dictionary storing stock prices
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "AMZN": 3500
}

portfolio = {}  # Dictionary to store user's stocks and quantities
total = 0  # Variable to store total investment

print(" Welcome to Stock Portfolio Tracker")

# Display available stocks
print("\nAvailable Stocks:")
for stock, price in stocks.items():
    print(f"{stock} : ${price}")

# Loop to take multiple inputs
while True:
    name = input("\nEnter stock name (or 'done'): ").upper()

    # Exit condition
    if name == "DONE":
        break

    # Check if stock exists
    if name in stocks:
        try:
            qty = int(input("Enter quantity: "))

            # Store in portfolio
            portfolio[name] = portfolio.get(name, 0) + qty

            # Calculate total
            total += stocks[name] * qty

            print(f" Added {qty} shares of {name}")

        except ValueError:
            print(" Please enter a valid number!")

    else:
        print(" Stock not found! Try again.")

# Display portfolio summary
print("\n Your Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stocks[stock]
    value = price * qty
    print(f"{stock} - {qty} shares × ${price} = ${value}")

# Display total investment
print("\n Total Investment:", total)

# Save to file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    for stock, qty in portfolio.items():
        file.write(f"{stock} : {qty} shares\n")
    file.write(f"Total Investment: ${total}")

print(" Portfolio saved to 'portfolio.txt'")