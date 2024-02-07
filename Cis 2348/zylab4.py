import math

wall_height = float(input("Enter wall height (feet):\n"))
wall_width = float(input("Enter wall width (feet):\n"))

wall_area = wall_height * wall_width
print(f"Wall area: {wall_area} square feet")

coverage_per_gallon = 350

paint_needed =wall_area / coverage_per_gallon
print(f"Paint needed: {paint_needed:.2f} gallons")

can_needed = math.ceil(paint_needed)
print(f"Cans needed: {cans_needed} can(s)")

paint_costs = {
    'red': 35,
    'blue': 25,
    'green': 23
}

paint_color = input("Choose a color to paint the wall:\n").lower()

if paint_color in paint_costs:
    total_cost = (cans_needed * paint_costs[paint_color])
   print(f"Cost of purchasing {paint_color} paint: ${total_cost}")
else:
    print("Sorry, that color is not available.")
