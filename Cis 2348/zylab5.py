services = {
    "Oil change": 35,
    "Tire rotation": 19,
    "Car wash": 7,
    "Car wax": 12
}

def output_menu():
    print("Day's auto shop services")
    for service, cost in services.items():
        print(f"{service} -- ${cost}")

def select_services():
    first_service = input("Select first service:\n")
    second_service = input("Select second service:\n")
    return first_service, second_service

def output_invoice(first_service, second_service):
    total_cost = 0
    print("\nDay's auto shop invoice")
    if first_service in services:
        print(f"Service 1: {first_service}, ${services[first_service]}")
        total_cost += services[first_service]
    elif first_service == "-":
        print("Service 1: No service")
        
    if second_service in services:
        print(f"Service 2: {second_service}, ${services[second_service]}")
        total_cost += services[second_service]
    elif second_service == "-":
        print("Service 2: No service")
        
    print(f"Total: ${total_cost}")

output_menu()
first_service, second_service = select_services()
output_invoice(first_service, second_service)