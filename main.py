import csv

# Define color codes (ANSI Format)
GREEN = "\033[32m"    # Available seat
RED = "\033[31m"      # booked seat
YELLOW = "\033[32m"   # Reserved seat
BLUE = "\033[34m"     # VIP seat
RESET = "\033[39m"    # Reset color

print("Welcome to my Airplane Seat Booking Manager!")
print("Hello World")
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
        seating_chart[i][j] = GREEN + "A" + RESET

# Function to display the seating chart with color-coded seats using a nested loop
def display_chart():
    for i in range(5):
        print(seating_chart[i])
        
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

# Main program loop
def main():
    loop = True
    while loop == True:
        previous = input("Would you like to work with the previous seating list? Enter yes or no: ")
        previous = previous.lower()
        if previous == "yes":
            open_file()
            display_chart()
        elif previous == "no":
            display_chart()
        else:
            print("Invalid input")
            continue
        action = input("Are you booking, reserving, marking a seat as VIP or Freeing up a seat. Enter booking, reserving, vip or free: ")
        action = action.lower()
        if action == "booking":
            row  = int(input("Which row would you like to book? 1-5"))
            row = row - 1
            column = int(input("Which column would you like to book? 1-5"))
            column = column - 1
            book_seat(row, column)
            save_file()
        elif action == "reserving":
            row  = int(input("Which row would you like to reserve? 1-5"))
            row = row - 1
            column = int(input("Which column would you like to reserve? 1-5"))
            column = column - 1
            reserve_seat(row, column)
            save_file()
        elif action == "vip":
            row  = int(input("Which row would you like to mark as vip? 1-5"))
            row = row - 1
            column = int(input("Which column would you like to mark as vip? 1-5"))
            column = column - 1
            vip_seat(row, column)
            save_file()
        elif action == "free":
            row  = int(input("Which row would you like to free? 1-5"))
            row = row - 1
            column = int(input("Which column would you like to free? 1-5"))
            column = column - 1
            free_seat(row, column)
            save_file()
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
