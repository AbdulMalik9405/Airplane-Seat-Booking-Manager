import csv

# Define color codes (ANSI Format)
GREEN = "\033[32m"    # Available seat
RED = "\033[31m"      # booked seat
YELLOW = "\033[33m"   # Reserved seat
BLUE = "\033[34m"     # VIP seat
RESET = "\033[39m"    # Reset color

print("Welcome to my Airplane Seat Booking Manager!")

# Create a seating chart (e.g. 5x5) using a 2D list
seating_chart = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]
# Set all seats as "available"
for i in range(5):
    for j in range(5):
        seating_chart[i][j] = "A"

# Function to display the seating chart with color-coded seats using a nested loop
def display_chart():
    for i in range(5):
        for j in range(5):
            if seating_chart[i][j] == "A":
                print(f"{GREEN}A{RESET}", end="\t")
            elif seating_chart[i][j] == "B":
                print(f"{RED}B{RESET}", end="\t")
            elif seating_chart[i][j] == "R":
                print(f"{YELLOW}R{RESET}", end="\t")
            elif seating_chart[i][j] == "V":
                print(f"{BLUE}V{RESET}", end="\t")
        print()
# Function to book a seat
def book_seat(row, column):
    seating_chart[row][column] = "B"

# Function to reserve a seat
def reserve_seat(row, column):
    seating_chart[row][column] = "R"

# Function to mark a seat as VIP
def vip_seat(row, column):
    seating_chart[row][column] = "V"

# Function to free up a seat
def free_seat(row, column):
    seating_chart[row][column] = "A"

# Function to save seating chart to a file
def save_file():
    with open("seating_chart.txt", "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(seating_chart)

# Function to load seating chart from a file
def open_file():
    global seating_chart
    temp_file = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]
    file = open("seating_chart.txt", "r")
    for i in range(5):
        line = file.readline()
        temp_file = line[0:9:2]
        temp_file = list(temp_file)
        for j in range(5):
            seating_chart[i][j] = temp_file[j]
    file.close

def change_seat(row, column):
    global Available, Booked, Reserved, VIP
    if seating_chart[row][column] == "A":
        Available = Available - 1
    elif seating_chart[row][column] == "B":
        Booked = Booked - 1
    elif seating_chart[row][column] == "R":
        Reserved = Reserved - 1
    else:
        VIP = VIP - 1

Available = 0
Booked = 0
Reserved = 0
VIP = 0

# Main program loop
def main():
    global Available, Booked, Reserved, VIP
    previous_chart = True
    while previous_chart == True:
        previous = input("Would you like to work with the previous seating list? Enter yes or no: ")
        previous = previous.lower()
        if previous == "yes":
            previous_chart = False
            open_file()
            display_chart()
        elif previous == "no":
            previous_chart = False
            display_chart()
        else:
            print("Invalid input")
            previous_chart = True
    for i in range(5):
        for j in range(5):
            if seating_chart[i][j] == "A":
                Available = Available + 1
            elif seating_chart[i][j] == "B":
                Booked = Booked + 1
            elif seating_chart[i][j] == "R":
                Reserved = Reserved + 1
            else:
                VIP = VIP + 1
    loop = True
    while loop == True:
        print("There are ", Available, " number of seats available. ", Booked, "Number of seats booked. ",Reserved, "Number of seats reserved.", VIP, "Number of VIP seats." )
        action = input("Are you booking, reserving, marking a seat as VIP or Freeing up a seat. Enter booking, reserving, vip or free: ")
        action = action.lower()
        if action == "booking":
            row  = int(input("Which row would you like to book? 1-5"))
            row = row - 1
            column = int(input("Which column would you like to book? 1-5"))
            column = column - 1
            change_seat(row, column)
            book_seat(row, column)
            save_file()
            Booked = Booked + 1
        elif action == "reserving":
            row  = int(input("Which row would you like to reserve? 1-5"))
            row = row - 1
            column = int(input("Which column would you like to reserve? 1-5"))
            column = column - 1
            change_seat(row, column)
            reserve_seat(row, column)
            save_file()
            Reserved = Reserved + 1
        elif action == "vip":
            row  = int(input("Which row would you like to mark as vip? 1-5"))
            row = row - 1
            column = int(input("Which column would you like to mark as vip? 1-5"))
            column = column - 1
            change_seat(row, column)
            vip_seat(row, column)
            save_file()
            VIP = VIP + 1
        elif action == "free":
            row  = int(input("Which row would you like to free? 1-5"))
            row = row - 1
            column = int(input("Which column would you like to free? 1-5"))
            column = column - 1
            change_seat(row, column)
            free_seat(row, column)
            save_file()
            Available = Available + 1
        else:
            print("Invalid input")
            continue
        edit = input("Would you like to continue editng the seating chart? Enter yes or no: ")
        edit = edit.lower()
        if edit == "yes":
            loop = True
        elif edit == "no":
            loop = False
        else:
            continue
        display_chart()

main()
