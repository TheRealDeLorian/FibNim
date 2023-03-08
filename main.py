#! /usr/bin/env python3
#fibonacci nim according to a wikipedia article I found
#Made from the bottom up by Dorian Cottle
#March 7th, 2023

def get_int(min, max):
    i = 1
    while i == 1:
        userinput = input(f"Choose wisely... Please enter a number between {min} and {max}.")
        if not userinput.isdigit():
            print("You must input an integer.")
        elif int(userinput) < min or int(userinput) > max:
            print(f"Must be between {min} and {max}, bro.")
            continue
        else:
            return int(userinput)

def swap_player(curplayer, p1, p2):
    if curplayer == p1:
        return p2
    elif curplayer == p2:
        return p1

def main():
    print("welcome to stick game!")
    print("In the first turn, player 1 is allowed to take as many sticks as they want, but not all.")
    print("In every other turn, you are allowed to take up to twice as many sticks as the player before you.")

    player1 = input("Player 1, what is your name?")
    player2 = input("Player 2, what are you called?")
    print(f"{player1} vs {player2}")
    print("How many sticks shall be played with?")
    totalsticks = get_int(3, 100)
    sticksremoved = 0

    turn = 1
    currentplayer = player1

    while totalsticks > 0:
        print(f"{currentplayer}, how many sticks would you like to remove?")
        if turn == 1:
            sticksremoved = get_int(1, totalsticks - 1)
        else:
            if sticksremoved*2 < totalsticks:
                sticksremoved = get_int(1, sticksremoved * 2)
            else:
                sticksremoved = get_int(1, totalsticks)
        totalsticks -= sticksremoved
        if totalsticks < 0:
            break
        print(f"{totalsticks} sticks left.")
        turn = turn + 1
        currentplayer = swap_player(currentplayer, player1, player2)

    currentplayer = swap_player(currentplayer, player1, player2)
    print(f"{currentplayer} wins in {turn} turns!")

if __name__ == "__main__":
    main()