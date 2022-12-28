from random import randint
from ten_thousand.game_logic import GameLogic


def default_roller():
    return GameLogic.roll_dice(6)


def play_dice(roller=default_roller):

    while True:
        print("Enter r to roll or q to quit")
        choice = input("> ")

        if choice == "q":
            print("OK, bye")
            break
        else:
            roll = roller()
            roll_str = ""
            for num in roll:
                roll_str += str(num) + " "
            print(f"*** {roll_str}***")


if __name__ == "__main__":
    rolls = [(1, 1, 1, 6, 4, 3)]

    def mock_roller():
        return rolls.pop(0) if rolls else default_roller()

    play_dice(mock_roller)
