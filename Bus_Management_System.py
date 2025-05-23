class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0
    
    def available_seats(self):
        return self.total_seats - self.booked_seats
    
    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            return True
        return False
    
    def __str__(self):
        self.fare = 500  # fixed vara 500
        return f"Bus Number: {self.number} | Route: {self.route} | Available: {self.available_seats()}/{self.total_seats} | Fare: {self.fare} BDT "


class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus
        self.fare = 500  # fixed vara 500
    
    def __str__(self):
        return f"Passenger: {self.name} | Phone: {self.phone} | Bus: {self.bus.number} | Fare: {self.fare} BDT"


class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self, username, password):
        return self.username == username and self.password == password


class BusSystem:
    def __init__(self):
        self.buses = []
        self.passengers = []
        self.admin = Admin("admin", "1234")
        self.admin_logged_in = False
    
    def add_bus(self, number, route, seats):

        new_bus = Bus(number, route, seats)
        self.buses.append(new_bus)
        print(f"Bus #{number} added successfully.")
        return True
    
    def find_bus(self, bus_number):
        for bus in self.buses:
            if bus.number == int(bus_number):
                return bus
        return None
    
    def book_ticket(self, bus_number, name, phone):
        bus = self.find_bus(bus_number)
        if not bus:
            print(f"No bus found with number {bus_number}.")
            return False
        
        if bus.book_seat():
            passenger = Passenger(name, phone, bus)
            self.passengers.append(passenger)
            print("\n----------- Ticket Booked Successfully -----------")
            print(f"Passenger: {name}")
            print(f"Phone: {phone}")
            print(f"Bus: {bus_number} | Route: {bus.route}")
            print(f"Fare: 500 taka only")
            print("Have e safe journey! Thanks for travelling with us.")
            print("---------------------------------------------------\n")
            return True
        else:
            print(f"Sorry, Bus #{bus_number} is fully booked.")
            return False
    
    def show_buses(self):
        if not self.buses:
            print("No buses available.")
            return
        
        print("\n--- Available Buses ---")
        counter = 1
        for bus in self.buses:
            print(f"{counter}. {bus}")
            counter += 1
        print("-------------------------\n")
    
    def admin_login(self, username, password):
        if self.admin.login(username, password):
            self.admin_logged_in = True
            print("Admin login successful!")
            return True
        else:
            print("Invalid username or password.")
            return False
    
    def admin_logout(self):
        self.admin_logged_in = False
        print("Admin logged out successfully.")


def main():
    bus_system = BusSystem()
    
    while True:
        print("\n=== Bus Management System ===")
        print("1. Admin Login")
        print("2. Book Ticket")
        print("3. View Buses")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            
            if choice == 1:
                username = input("Enter username: ")
                password = input("Enter password: ")
                if bus_system.admin_login(username, password):
                    admin_menu(bus_system)
            
            elif choice == 2:
                if not bus_system.buses:
                    print("No buses available for booking.")
                    continue
                
                bus_system.show_buses()
                bus_number = int(input("Enter bus number: "))
                name = input("Enter passenger name: ")
                phone = input("Enter passenger phone number: ")
                
                if not name or not phone:
                    print("Name and phone cannot be empty.")
                    continue
                
                bus_system.book_ticket(bus_number, name, phone)
            
            elif choice == 3:
                bus_system.show_buses()
            
            elif choice == 4:
                print("Thank you for using the Bus Management System!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        
        except ValueError:
            print("Please enter a valid number.")


def admin_menu(bus_system):
    while bus_system.admin_logged_in:
        print("\n=== Admin Menu ===")
        print("1. Add Bus")
        print("2. View All Buses")
        print("3. Logout")
        
        try:
            choice = int(input("Enter your choice (1-3): "))
            
            if choice == 1:
                bus_number = int(input("Enter bus number: "))
                route = input("Enter bus route: ")

                seats = int(input("Enter total seats: "))
                if seats <= 0:
                    print("Number of seats must be positive.")
                    continue
                    
                bus_system.add_bus(bus_number, route, seats)

            elif choice == 2:
                bus_system.show_buses()
            
            elif choice == 3:
                bus_system.admin_logout()
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        
        except ValueError:
            print("Please enter a valid number.")

main()