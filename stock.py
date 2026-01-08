# Step 1: Hardcoded stock prices (Dictionary)
stock_prices = {
    "AAPL": 180,
    "GOOGL": 140,
    "MSFT": 320,
    "TSLA": 250,
    "AMZN": 135
}

portfolio = []          # To store stock details
total_investment = 0    # Total investment value

print("📊 Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))

# Step 2: Take user input
while True:
    stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    # Step 3: Check if stock exists
    if stock_name in stock_prices:
        quantity = input("Enter quantity: ")

        if quantity.isdigit():
            quantity = int(quantity)
            price = stock_prices[stock_name]
            investment = price * quantity

            total_investment += investment
            portfolio.append([stock_name, quantity, price, investment])

            print(f"Added {quantity} shares of {stock_name}")
        else:
            print("❌ Quantity must be a number.")
    else:
        print("❌ Stock not available.")

# Step 4: Display portfolio summary
print("\n📁 Portfolio Summary")
print("-" * 40)

for stock in portfolio:
    print(f"Stock: {stock[0]} | Qty: {stock[1]} | Price: ₹{stock[2]} | Value: ₹{stock[3]}")

print("-" * 40)
print("💰 Total Investment Value: ₹", total_investment)

# Step 5: Save result to file
save_choice = input("\nDo you want to save the result? (yes/no): ").lower()

if save_choice == "yes":
    file_type = input("Choose file type (txt/csv): ").lower()

    if file_type == "txt":
        with open("portfolio.txt", "w") as file:
            file.write("Stock,Quantity,Price,Investment\n")
            for stock in portfolio:
                file.write(f"{stock[0]},{stock[1]},{stock[2]},{stock[3]}\n")
            file.write(f"Total,,,{total_investment}")
        print("✅ Saved to portfolio.txt")

    elif file_type == "csv":
        with open("portfolio.csv", "w") as file:
            file.write("Stock,Quantity,Price,Investment\n")
            for stock in portfolio:
                file.write(f"{stock[0]},{stock[1]},{stock[2]},{stock[3]}\n")
            file.write(f"Total,,,{total_investment}")
        print("✅ Saved to portfolio.csv")

    else:
        print("❌ Invalid file type.")
