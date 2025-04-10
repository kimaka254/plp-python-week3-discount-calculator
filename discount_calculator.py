# Week 3 Assignment - PLP Python Programming

# Function for calculating discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Prompting the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    # Calculate and display final price
    final_price = calculate_discount(original_price, discount)

    if discount >= 20:
        print(f"Discount applied. Final price: KES {final_price:.2f}")
    else:
        print(f"No discount applied. Final price: KES {final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")
