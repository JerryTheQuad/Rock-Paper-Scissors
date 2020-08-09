import random

list_ = ['scissors', 'rock', 'paper']

lose_conditions = {'rock': 'paper', 'scissors': 'rock', 'paper': 'scissors'}

name = input('Enter your name: ')
print(f'Hello, {name}')


def add_player(name_4):
    with open('rating.txt', 'a') as file_1:
        file_1.write(f"{name_4} 0\n")


with open('rating.txt', 'w') as file_write:
    with open('rating.txt', 'r') as file_rating:
        fr = file_rating.readlines()
        if name not in fr:
            add_player(name)


def add_rating(rating_2):
    with open('rating.txt', 'r') as readfile:
        rd = readfile.readlines()
        for line_2 in rd:
            if name in line_2:
                c = rd.index(line_2)
                name_2, score = line_2.split()
                score_1 = int(score) + rating_2
                rd[c] = f"{name_2} {score_1}\n"
        with open('rating.txt', 'w') as writefile:
            writefile.writelines(rd)


number_of_options = input()
number_of_options_list = number_of_options.split(',')

print("Okay, let's start")

while True:
    player = input()

    if player == '!exit':
        print('Bye!')
        break

    elif player == '!rating':
        with open('rating.txt', 'r') as rating:
            for line in rating:
                if name in line:
                    name_1, rat = line.split()
        print(f'Your rating: {rat}')

    elif player not in list_ and player not in number_of_options_list:
        print('Invalid input')

    elif len(number_of_options) == 0:
        if player in list_:
            a = lose_conditions[player]
            computer = random.choice(list_)
            if player == computer:
                add_rating(50)
                print(f'There is a draw ({computer})')
            elif a == computer:
                print(f'Sorry, but computer chose {computer}')
            elif a != computer:
                add_rating(100)
                print(f'Well done. Computer chose {computer} and failed')

    elif len(number_of_options) > 0:
        computer_1 = random.choice(number_of_options_list)
        where_player = number_of_options_list.index(player)
        complete_list = number_of_options_list[where_player + 1:] + number_of_options_list[0: where_player]
        if computer_1 == player:
            add_rating(50)
            print(f'There is a draw ({computer_1})')
        elif computer_1 in complete_list[0:8]:
            print(f'Sorry, but computer chose {computer_1}')
        elif computer_1 in complete_list[8:]:
            add_rating(100)
            print(f'Well done. Computer chose {computer_1} and failed')

