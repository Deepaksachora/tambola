import numpy as np
import tabulate

ticket_array = np.zeros((3,9), dtype=int )

#Randomly Generate 15 indices to fill values in a ticket.

total_indices = [(i,j) for i in range(3) for j in range(9)]

random_indices = []

first_row = random_indices.sample(total_indices[:9], 5)
second_row = random_indices.sample(total_indices[9:18], 5)
third_row = random_indices.sample(total_indices[-9:], 5)

for i in first_row, second_row, third_row:
    random_indices.append(i)

#Now fill these indices with random values

for num in random_indices:
    if num[1] == 0:
        number = random.choice(total_number[:10])
        ticket_array[num] = number
        total_numbers[total_numbers.index(number)] = 0
    
    elif num[1] == 1:
        number = random.choice(total_number[10:20])
        ticket_array[num] = number
        total_numbers[total_numbers.index(number)] = 0

    elif num[1] == 2:
        number = random.choice(total_number[20:30])
        ticket_array[num] = number
        total_numbers[total_numbers.index(number)] = 0

    elif num[1] == 3:
        number = random.choice(total_number[30:40])
        ticket_array = number
        total_numbers[total_numbers.index(number)] = 0

    elif num[1] == 4:
        number = random.choice(total_number[40:50])
        ticket_array = number
        total_numbers[total_numbers.index(number)] = 0

    elif num[1] == 5:
        number = random.choice(total_number[50:60])
        ticket_array = number
        total_numbers[total_numbers.index(number)] = 0

    elif num[1] == 6:
        number = random.choice(total_number[60:70])
        ticket_array = number
        total_numbers[total_numbers.index(number)] = 0

    elif num[1] == 7:
        number = random.choice(total_number[70:80])
        ticket_array = number
        total_numbers[total_numbers.index(number)] = 0

    elif num[1] == 8:
        number = random.choice(total_number[80:89])
        ticket_array = number
        total_numbers[total_numbers.index(number)] = 0


#Now let's sort the ticket_array column-wise
for col in range(9):

    #if all the rows are fill with random no.
    if (ticket_array[0][col] != 0 and ticket_array[1][col] != 0 and ticket_array[1][col] != 0):
        for row in range(2):
            if ticket_array[row][col] > ticket_array[row+1][col]:
                temp = ticket_array[row][col]
                ticket_array[row][col] = ticket_array[row+1][col]
                ticket_array[row+1][col] = temp

    # if 1st and 2nd row are filled by random number
    elif(ticket_array[0][col] != 0 and ticket_array[1][col] != 0 and ticket_array[2][col] == 0):
        if ticket_array[0][col] > ticket_array[1][col]:
            temp = ticket_array[0][col]
            ticket_array[0][col] = ticket_array[1][col]
            ticket_array[1][col] = temp
    # if 1st and 3rd row are filled by random number
    elif(ticket_array[0][col] != 0 and ticket_array[2][col] != 0 and ticket_array[1][col] == 0):
        if ticket_array[0][col] > ticket_array[2][col]:
            temp = ticket_array[0][col]
            ticket_array[0][col] = ticket_array[2][col]
            ticket_array[2][col] = temp

    # if 2nd and 3rd rows are filled with random numbers
    elif(ticket_array[0][col] == 0 and ticket_array[1][col] != 0 and ticket_array[2][col] != 0):
        if ticket_array[1][col] > ticket_array[2][col]:
            temp = ticket_array[1][col]
            ticket_array[1][col] = ticket_array[2][col]
            ticket_array[2][col] = temp

if __name__ == "__main__":
        
    # Take number of tickets from user as system argument
    numberOfTickets = sys.argv[1]
    tickets = []

    for i in range(int(numberOfTickets)):
        ticket = getTickets()
        tickets.append(ticket)

    for ticket in tickets:
        print(tabulate(ticket, tablefmt="fancy_grid", numalign="center"))        


