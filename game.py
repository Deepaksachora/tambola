import random
import string

import numpy as np


class Game:
    def __init__(self, admin_ip):
        self._users = []
        self._tables = {}
        self._admin_ip = admin_ip
        self._started = False
        self._id = random.randint(100, 999)

    def generate_number(self):
        pass

    def get_id(self):
        return self._id

    def start_game(self):
        self._started = True

    def is_active(self):
        return self._started

    def is_admin(self, admin_ip):
        return self._admin_ip == admin_ip

    def create_user(self):
        code = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        self._users.append(code)
        return code

    def generate_board(self, user_id):
        if user_id not in self._users:
            raise ValueError("USER INVALID")

        # create 2d array of dim 3x9
        ticket_array = np.zeros((3, 9), dtype=int)
        total_indices = [(i, j) for i in range(3) for j in range(9)]

        random_indices = []

        # Pick 5 random blocks in each row
        first = random.sample(total_indices[:9], 5)
        second = random.sample(total_indices[9:18], 5)
        third = random.sample(total_indices[-9:], 5)

        for i in first:
            random_indices.append(i)

        for i in second:
            random_indices.append(i)

        for i in third:
            random_indices.append(i)

        total_numbers = [i for i in range(1, 91)]
        for num in random_indices:
            if num[1] == 0:
                number = random.choice(total_numbers[:10])
                ticket_array[num] = number
                total_numbers[total_numbers.index(number)] = 0
            elif num[1] == 1:
                number = random.choice(total_numbers[10:20])
                ticket_array[num] = number
                total_numbers[total_numbers.index(number)] = 0
            elif num[1] == 2:
                number = random.choice(total_numbers[20:30])
                ticket_array[num] = number
                total_numbers[total_numbers.index(number)] = 0
            elif num[1] == 3:
                number = random.choice(total_numbers[30:40])
                ticket_array[num] = number
                total_numbers[total_numbers.index(number)] = 0
            elif num[1] == 4:
                number = random.choice(total_numbers[40:50])
                ticket_array[num] = number
                total_numbers[total_numbers.index(number)] = 0
            elif num[1] == 5:
                number = random.choice(total_numbers[50:60])
                ticket_array[num] = number
                total_numbers[total_numbers.index(number)] = 0
            elif num[1] == 6:
                number = random.choice(total_numbers[60:70])
                ticket_array[num] = number
                total_numbers[total_numbers.index(number)] = 0
            elif num[1] == 7:
                number = random.choice(total_numbers[70:80])
                ticket_array[num] = number
                total_numbers[total_numbers.index(number)] = 0
            elif num[1] == 8:
                number = random.choice(total_numbers[80:89])
                ticket_array[num] = number
                total_numbers[total_numbers.index(number)] = 0

            for col in range(9):

                # if all the rows are filled with random number
                if ticket_array[0][col] != 0 and ticket_array[1][col] != 0 and ticket_array[2][col] != 0:
                    for row in range(2):
                        if ticket_array[row][col] > ticket_array[row + 1][col]:
                            temp = ticket_array[row][col]
                            ticket_array[row][col] = ticket_array[row + 1][col]
                            ticket_array[row + 1][col] = temp


                # if 1st and 2nd row are filled by random number
                elif ticket_array[0][col] != 0 and ticket_array[1][col] != 0 and ticket_array[2][col] == 0:
                    if ticket_array[0][col] > ticket_array[1][col]:
                        temp = ticket_array[0][col]
                        ticket_array[0][col] = ticket_array[1][col]
                        ticket_array[1][col] = temp


                # if 1st and 3rd row are filled by random number
                elif ticket_array[0][col] != 0 and ticket_array[2][col] != 0 and ticket_array[1][col] == 0:
                    if ticket_array[0][col] > ticket_array[2][col]:
                        temp = ticket_array[0][col]
                        ticket_array[0][col] = ticket_array[2][col]
                        ticket_array[2][col] = temp

                # if 2nd and 3rd rows are filled with random numbers

                elif ticket_array[0][col] == 0 and ticket_array[1][col] != 0 and ticket_array[2][col] != 0:
                    if ticket_array[1][col] > ticket_array[2][col]:
                        temp = ticket_array[1][col]
                        ticket_array[1][col] = ticket_array[2][col]
                        ticket_array[2][col] = temp

        self._tables[user_id] = ticket_array
        return ticket_array
