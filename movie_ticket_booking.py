# Movie Ticket Booking Management

# Dictionary to store booking details
bookings = {}

# Function to create a new booking
def create_booking():
booking_id = input("Enter Booking ID: ")
if booking_id in bookings:
print("Booking ID already exists. Please try again.")
else:
name = input("Enter Name: ")
movie_name = input("Enter Movie Name: ")
num_tickets = int(input("Enter Number of Tickets: "))
bookings[booking_id] = {
"Name": name,
"Movie Name": movie_name,
"Number of Tickets": num_tickets,
}
print("Booking created successfully!")

# Function to view all bookings
def read_bookings():
if not bookings:
print("No bookings available.")
else:
print("\nCurrent Bookings:")
for booking_id, details in bookings.items():
print(f"Booking ID: {booking_id}")
for key, value in details.items():
print(f" {key}: {value}")
print()

# Function to update an existing booking
def update_booking():
booking_id = input("Enter Booking ID to update: ")
if booking_id not in bookings:
print("Booking ID not found.")
else:
print("What do you want to update?")
print("1. Name")
print("2. Movie Name")
print("3. Number of Tickets")
choice = input("Enter your choice: ")
if choice == "1":
bookings[booking_id]["Name"] = input("Enter new Name: ")
elif choice == "2":
bookings[booking_id]["Movie Name"] = input("Enter new Movie Name: ")
elif choice == "3":
bookings[booking_id]["Number of Tickets"] = int(input("Enter new Number of Tickets: "))
else:
print("Invalid choice.")
print("Booking updated successfully!")

# Function to delete a booking
def delete_booking():
booking_id = input("Enter Booking ID to delete: ")
if booking_id not in bookings:
print("Booking ID not found.")
else:
del bookings[booking_id]
print("Booking deleted successfully!")

# Main menu function
def menu():
while True:
print("\n--- Movie Ticket Booking Management ---")
print("1. Create Booking")
print("2. View Bookings")
print("3. Update Booking")
print("4. Delete Booking")
print("5. Exit")
choice = input("Enter your choice: ")
if choice == "1":
create_booking()
elif choice == "2":
read_bookings()
elif choice == "3":
update_booking()
elif choice == "4":
delete_booking()
elif choice == "5":
print("Exiting the program. Goodbye!")
break
else:
print("Invalid choice. Please try again.")

# Run the program
menu()
