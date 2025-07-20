# CloudFare Airlines - Flight Reservation System (Allowed Methods Only)

# --- Data Storage ---
flights = {}       # Stores flight details
customers = {}     # Stores customer details
bookings = []      # Stores bookings

# --- Constants ---
USERNAME = "Staff"
PASSWORD = "Cloud123"
MAX_ECONOMY = 5
MAX_BUSINESS = 3
ECONOMY_FARE = 500
BUSINESS_FARE = 1000

# --- Login (Figure 1) ---
def login():
    print("\n" + "-" * 50)
    print("CloudFare Airlines\nStaff Login")
    print("-" * 50)

    choice = input("Do you want to login (Yes/No)? ")
    if choice == "Yes" or choice == "yes":
        username = input("Username - ")
        password = input("Password - ")
        if username == USERNAME and password == PASSWORD:
            print("Login successful.\n")
            return True
        else:
            print("Invalid credentials.\n")
            return False
    return False

# --- Main Menu (Figure 2) ---
def main_menu():
    while True:
        print("-" * 50)
        print("CloudFare Airlines\nMain Menu")
        print("-" * 50)
        print("1) Add flight details")
        print("2) Register a customer")
        print("3) Search for available flight details")
        print("4) Booking a flight")
        print("5) View booking details")
        print("6) Exit")

        choice = input("\nYour Choice: ")

        if choice == '1':
            add_flight()
        elif choice == '2':
            register_customer()
        elif choice == '3':
            search_flight()
        elif choice == '4':
            book_flight()
        elif choice == '5':
            view_bookings()
        elif choice == '6':
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid option.\n")

# --- Add Flight (Figure 3) ---
def add_flight():
    print("\nCloudFare Airlines\nAdd flight details")

    flight_no = input("1) Flight No - ")
    departure = "JFK"  # Always fixed
    arrival = input("3) Arrival (To) - ")
    date = input("4) Departure Date - ")
    time = input("5) Departure Time - ")

    flights[flight_no] = {
        "from": departure,
        "to": arrival,
        "date": date,
        "time": time,
        "eco_seats": MAX_ECONOMY,
        "bus_seats": MAX_BUSINESS
    }

    print("6) Total no of economy class seats  -", MAX_ECONOMY)
    print("7) Total no of business class seats -", MAX_BUSINESS)
    print("8) Fare for an economy class person  - $", ECONOMY_FARE)
    print("9) Fare for a business class person  - $", BUSINESS_FARE)

    confirm = input("Do you want to add (Yes/No)? ")
    if confirm == "Yes":
        print("Flight added successfully.\n")
    else:
        flights.pop(flight_no)
        print("Flight not added.\n")

# --- Register Customer (Figure 4) ---
def register_customer():
    print("\nCloudFare Airlines\nRegister Customer")

    cust_id = input("Customer ID - ")
    name = input("Name - ")
    passport = input("Passport Number - ")
    address = input("Address - ")
    phone = input("Telephone Number - ")

    customers[cust_id] = {
        "name": name,
        "passport": passport,
        "address": address,
        "phone": phone
    }

    confirm = input("Do you want to save (Yes/No)? ")
    if confirm == "Yes":
        print("Customer saved successfully.\n")
    else:
        customers.pop(cust_id)
        print("Customer not saved.\n")

# --- Search Flight (Figure 5) ---
def search_flight():
    print("\nCloudFare Airlines\nSearch for available flights")

    date = input("1) Departure Date - ")
    time = input("2) Departure Time - ")
    from_city = input("3) Flying From - ")
    to_city = input("4) Flying To - ")
    travel_class = input("6) Travel Class (Business Class/Economy Class) - ")

    found = False
    for flight_no in flights:
        flight = flights[flight_no]
        if flight["date"] == date and flight["time"] == time and flight["from"] == from_city and flight["to"] == to_city:
            print("5) Flight No -", flight_no)
            if travel_class == "Business Class":
                print("7) No of seats available in the flight -", flight["bus_seats"])
            elif travel_class == "Economy Class":
                print("7) No of seats available in the flight -", flight["eco_seats"])
            else:
                print("Invalid class.")
            found = True
            break
    if not found:
        print("No matching flights found.")
    input("Do you want to search (Yes/No)? ")

# --- Book Flight (Figure 6) ---
def book_flight():
    print("\nCloudFare Airlines\nBooking a flight")

    flight_no = input("1) Flight No - ")
    if flight_no not in flights:
        print("Flight not found.\n")
        return

    name = input("2) Customer Name - ")
    passport = input("3) Passport Number - ")
    destination = flights[flight_no]["to"]
    date = flights[flight_no]["date"]
    time = flights[flight_no]["time"]
    travel_class = input("7) Travel Class (Business Class/ Economy Class) - ")

    if travel_class == "Business Class" and flights[flight_no]["bus_seats"] > 0:
        flights[flight_no]["bus_seats"] -= 1
    elif travel_class == "Economy Class" and flights[flight_no]["eco_seats"] > 0:
        flights[flight_no]["eco_seats"] -= 1
    else:
        print("Requested class not available.\n")
        return

    bookings.append([
        flight_no, name, passport, destination, date, time, travel_class
    ])

    confirm = input("Do you want to book (Yes/No)? ")
    if confirm == "Yes":
        print("Flight booked successfully.\n")
    else:
        bookings.pop()
        print("Booking cancelled.\n")

# --- View Bookings (Figure 7) ---
def view_bookings():
    print("\nCloudFare Airlines\nView booking details")

    target_date = input("Departure Date : ")
    print(f"\n{'Flight No':<10} {'Departure Time':<15} {'Destination':<15} {'No of passengers':<15}")

    for flight_no in flights:
        count = 0
        for booking in bookings:
            if booking[0] == flight_no and booking[4] == target_date:
                count += 1
        if count > 0:
            print(f"{flight_no:<10} {flights[flight_no]['time']:<15} {flights[flight_no]['to']:<15} {count:<15}")
    input("Do you want to view (Yes/No)? ")

# --- Start Program ---
if __name__ == "__main__":
    if login():
        main_menu()
    else:
        print("Access denied.")