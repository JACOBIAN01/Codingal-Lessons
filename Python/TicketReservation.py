print("Welcome to Sayantika Travels")

available_seats = [1,2,3,4,5,6,7,8,9,10]
reserved_seats = []

def bookTicket(seatNumber):
    available_seats.remove(seatNumber)
    reserved_seats.append(seatNumber)
    print(seatNumber," Reserved Successfully!")


def cancelTicket(seatNumber):
    reserved_seats.remove(seatNumber)
    available_seats.append(seatNumber)
    print(seatNumber," Canceled! ")

def ShowAvailableSeats():
    print("Available Seats are")
    print(available_seats)

choice = input("Enter Your Choice. 1.Book Ticket 2. Cancel Ticket 3. Show Ticket 4. Exit . Select(1/2/3/4): ")


while True:
    choice = int(input("Enter Your Choice. 1.Book Ticket 2. Cancel Ticket 3. Show Ticket . Select(1/2/3): "))
    if choice == 1:
        seatNumber = int(input("Enter Seat Number: "))
        bookTicket(seatNumber)
    elif choice == 2:
        seatNumber = int(input("Enter Seat Number: "))
        cancelTicket(seatNumber)
    elif choice == 3:
        ShowAvailableSeats()
    elif choice == 4:
        break
    else:
        print("Invalid")


