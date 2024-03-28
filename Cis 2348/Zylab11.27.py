roster = {}

for i in range(1, 6):
    jersey_number = int(input(f"Enter player {i}'s jersey number:\n"))
    rating = int(input(f"Enter player {i}'s rating:\n"))
    print()
    roster[jersey_number] = rating

print("ROSTER")
for jersey_number, rating in sorted(roster.items()):
    print(f"Jersey number: {jersey_number}, Rating: {rating}")

def print_menu():
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit\n")

def output_roster():
    print("\nROSTER")
    for jersey_number, rating in sorted(roster.items()):
        print(f"Jersey number: {jersey_number}, Rating: {rating}")

def add_player():
    new_jersey_number = int(input("Enter a new player's jersey number:\n"))
    new_rating = int(input("Enter the player's rating:\n"))
    roster[new_jersey_number] = new_rating

def remove_player():
    jersey_number_to_remove = int(input("Enter a jersey number:\n"))
    if jersey_number_to_remove in roster:
        del roster[jersey_number_to_remove]
    else:
        print("Jersey number not found in roster.")

def update_rating():
    jersey_number = int(input("Enter a jersey number:\n"))
    if jersey_number in roster:
        new_rating = int(input("Enter a new rating for player:\n"))
        roster[jersey_number] = new_rating
    else:
        print("Jersey number not found in roster.")

def output_above_rating():
    rating_threshold = int(input("Enter a rating:\n"))
    print(f"\nABOVE {rating_threshold}")
    for jersey_number, rating in sorted(roster.items()):
        if rating > rating_threshold:
            print(f"Jersey number: {jersey_number}, Rating: {rating}")

while True:
    print_menu()
    choice = input("Choose an option:\n")

    if choice == 'a':
        add_player()
    elif choice == 'd':
        remove_player()
    elif choice == 'u':
        update_rating()
    elif choice == 'r':
        output_above_rating()
    elif choice == 'o':
        output_roster()
    elif choice == 'q':
        break
    else:
        print("Invalid option. Please choose from the menu.")