from random import choices

x_o_list = []
block_list = []
position_dict = {}


def setup_board():
    global x_o_list
    global block_list

    block_list = ['TR', 'TM', 'TL', 'MR', 'MM', 'ML', 'BR', 'BM', 'BL']
    for position in block_list:
        position_dict[position] = " "
    x_o_list = ['X', 'O']


def print_board():
    print('\n')
    print(position_dict['TR'], '|', position_dict['TM'], '|', position_dict['TL'])
    print("--|---|--")
    print(position_dict["MR"], '|', position_dict['MM'], '|', position_dict['ML'])
    print("--|---|--")
    print(position_dict["BR"], '|', position_dict['BM'], '|', position_dict['BL'])
    print('\n')


def check_for_winner():

    # CHECK FOR WINNER TOP ROW
    if ord(position_dict['TR']) + ord(position_dict['TM']) + ord(position_dict['TL']) == 264 or \
            (ord(position_dict['TR']) + ord(position_dict['TM']) + ord(position_dict['TL'])) == 237:
        print(f"{position_dict['TR']} is the winner!!!")
        return 0

    # CHECK FOR WINNER MIDDLE ROW
    elif ord(position_dict['MR']) + ord(position_dict['MM']) + ord(position_dict['ML']) == 264 or \
            ord(position_dict['MR']) + ord(position_dict['MM']) + ord(position_dict['ML']) == 237:
        print(f"{position_dict['MR']} is the winner!!!")
        return 0

    # CHECK FOR WINNER BOTTOM ROW
    elif ord(position_dict['BR']) + ord(position_dict['BM']) + ord(position_dict['BL']) == 264 or \
            ord(position_dict['BR']) + ord(position_dict['BM']) + ord(position_dict['BL']) == 237:
        print(f"{position_dict['BR']} is the winner!!!")
        return 0

    # CHECK FOR WINNER TOP RIGHT TO BOTTOM LEFT
    elif ord(position_dict['TR']) + ord(position_dict['MM']) + ord(position_dict['BL']) == 264 or \
            ord(position_dict['TR']) + ord(position_dict['MM']) + ord(position_dict['BL']) == 237:
        print(f"{position_dict['TR']} is the winner!!!")
        return 0

    # CHECK FOR WINNER BOTTOM LEFT TO TOP LEFT
    elif ord(position_dict['BL']) + ord(position_dict['MM']) + ord(position_dict['TL']) == 264 or \
            ord(position_dict['BL']) + ord(position_dict['MM']) + ord(position_dict['TL']) == 237:
        print(f"{position_dict['BL']} is the winner!!!")
        return 0

    # CHECK FOR WINNER TOP RIGHT TO BOTTOM RIGHT
    elif ord(position_dict['TR']) + ord(position_dict['MR']) + ord(position_dict['BR']) == 264 or \
            ord(position_dict['TR']) + ord(position_dict['MR']) + ord(position_dict['BR']) == 237:
        print(f"{position_dict['TR']} is the winner!!!")
        return 0

    # CHECK FOR WINNER TOP MIDDLE TO BOTTOM MIDDLE
    elif ord(position_dict['TM']) + ord(position_dict['MM']) + ord(position_dict['BM']) == 264 or \
            ord(position_dict['TM']) + ord(position_dict['MM']) + ord(position_dict['BM']) == 237:
        print(f"{position_dict['TM']} is the winner!!!")
        return 0

    # CHECK FOR WINNER TOP LEFT TO BOTTOM LEFT
    elif ord(position_dict['TL']) + ord(position_dict['ML']) + ord(position_dict['BL']) == 264 or \
            ord(position_dict['TL']) + ord(position_dict['ML']) + ord(position_dict['BL']) == 237:
        print(f"{position_dict['TL']} is the winner!!!")
        return 0

    else:
        return 1


def pc_select():
    select = choices(block_list)
    return select[0]


def make_selection(x_o):
    count = 0
    player_turn = 0
    while count < 9:

        if player_turn == 0:
            select_block = input("Select block: ")
            player_turn = 1
            user_input = x_o

        else:
            select_block = pc_select()
            player_turn = 0
            user_input = x_o_list[0]

        # CHECK VALID BLOCK OPTION HAS BEEN SELECTED
        if select_block.upper() not in block_list:
            print("Incorrect selection!! Try again!!")
            make_selection(x_o)

        # CHECK BLOCK SELECTED IS EMPTY
        if position_dict[select_block.upper()] == "O" or position_dict[select_block.upper()] == "X":
            print("Block already selected!! Try again!!")
            make_selection(x_o)

        position_dict[select_block.upper()] = user_input.capitalize()
        block_list.remove(select_block.upper())

        print("Position Dict: ", position_dict)
        print_board()
        outcome = check_for_winner()
        if outcome == 0:
            return
        count += 1
        continue

    if count == 9:
        print("Sorry no winner!!")
        return


def main(name):

    setup_board()

    x_o = input("Do you want to be X or O? ")

    if x_o not in ('X', 'O', 'o', 'x'):
        print("Incorrect selection made!! Try again!!")
        main(name)

    x_o_list.remove(x_o.upper())
    print_board()
    make_selection(x_o)

    play_again = input("\nWant to play again? Y or N ")
    if play_again.upper() == 'Y':
        main(name)

    else:
        "See you next time!!"


print("\nWelcome to Tic-Tak-Toe\n")
name = input("Enter Player name: ")


print('\n')
print('Use below options to select block')
print('\n')
print('TR', '|', 'TM', '|', 'TL')
print("---|----|--")
print("MR", '|', 'MM', '|', 'ML')
print("---|----|--")
print("BR", '|', 'BM', '|', 'BL')
print('\n')


main(name)




