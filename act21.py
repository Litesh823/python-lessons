name = "Litesh"
num1 = 55
num2 = 25.275
isPresent = True

print(f"type of 'name' is {type(name).__name__}")
print(f"type of 'num1' is {type(num1).__name__}")
print(f"type of 'num2' is {type(num2).__name__}")
print(f"type of 'isPresent' is {type(isPresent).__name__}")

snack_name = "chips"
price = 1.5
quantity = 10
is_avaialble = True

# Part 2 - Arithematic OPERATORS
total = price * quantity
print("Total value: $", total)
print("Sale price: $", price - 0.25)
print("Double stock:", quantity * 2)

# PART 3 - COMPARISON OPERATORS
print("Is price under $2?", price < 2)
print("More than 5 in stock?", quantity > 5)
print("Is price exactly $1.50?", price == 1.50)

#PART 4 - STRING OPERATORS
shop_name = "Quick" + " " + "Bites"
print("Shop name:", shop_name)
print("Letters in snack name:", len(snack_name))
print("First letter:", snack_name[0])

# PART 5 - SWAPPING VALUES
price_a = 1.50
price_b = 3.00
print("Before:", price_a, "and", price_b)

temp = price_a
price_a = price_b
price_b = temp

print("After:", price_a, "and", price_b)