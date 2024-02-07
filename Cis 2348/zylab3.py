# This is a sample Python script.

def cups_to_gallons(cups):
    return cups / 16.0

lemon_juice_cups = float(input("Enter amount of lemon juice (in cups):\n"))
water_cups = float(input("Enter amount of water (in cups):\n"))
agave_nectar_cups = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n"))

print(f"\nLemonade ingredients - yields {servings:.2f} servings")
print(f"{lemon_juice_cups:.2f} cup(s) lemon juice")
print(f"{water_cups:.2f} cup(s) water")
print(f"{agave_nectar_cups:.2f} cups(s) agave nectar\n")

desired_servings = float(input("How many servings would you like to make?\n"))
lemon_juice_cups *= (desired_servings / servings)
water_cups *= (desired_servings / servings)
agave_nectar_cups *= (desired_servings / servings)

print(f"\nLemonade ingredients - yields {desired_servings:.2f} servings")
print(f"{lemon_juice_cups:.2f} cup(s) lemon juice")
print(f"{water_cups:.2f} cup(s) water")
print(f"{agave_nectar_cups:.2f} cup(s) agave nectar\n")

lemon_juice_gallons = cups_to_gallons(lemon_juice_cups)
water_gallons = cups_to_gallons(water_cups)
agave_nectar_gallons = cups_to_gallons(agave_nectar_cups)

print(f"\nLemonade ingredients - yields {desired_servings:.2f} servings")
print(f"{lemon_juice_gallons:.2f} gallon(s) lemon juice")
print(f"{water_gallons:.2f} gallon(s) water")
print(f"{agave_nectar_gallons:.2f} gallon(s) agave nectar")