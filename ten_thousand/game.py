from ten_thousand.game_logic import GameLogic

currently_playing = True


def intro():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    choice = input("> ")

    if choice == "n":
        print("OK. Maybe another time")
        global currently_playing
        currently_playing = False
    else:
        print(f"Starting round 1")


def default_roller(num):
    return GameLogic.roll_dice(num)


def play_dice(roller=default_roller):
    total_score = 0
    round_number = 1
    current_dice = []
    dice_roll = []
    round_score = 0

    while currently_playing:

        print(f"Rolling {6 - len(current_dice)} dice...")
        roll = roller(6 - len(current_dice))
        roll_str = ""
        roll_list = []
        for num in roll:
            roll_str += str(num) + " "
            roll_list.append(num)
        print(f"*** {roll_str}***")
        if GameLogic.calculate_score(tuple(roll_list)) == 0:
            print("You Zilch'd!")
            current_dice = []
            dice_roll = []
            round_score = 0
            round_number += 1
            print(f"Total score is {total_score} points")
            print(f"Starting round {round_number}")
        else:
            print("Enter dice to keep, or (q)uit:")

            keep = input("> ")
            if keep == "q":
                print(f"Thanks for playing. You earned {total_score} points")
                break
            for character in keep:
                current_dice.append(int(character))
                dice_roll.append(int(character))
            round_score += GameLogic.calculate_score(tuple(dice_roll))
            print(f"You have {round_score} unbanked points and {6 - len(current_dice)} dice remaining")
            print(f"(r)oll again, (b)ank your points or (q)uit:")
            choice = input("> ")
            if choice == "b":
                print(f"You banked {round_score} points in round {round_number}")
                total_score += round_score
                print(f"Total score is {total_score} points")
                current_dice = []
                round_score = 0
                round_number = round_number + 1
                print(f"Starting round {round_number}")
            if choice == "q":
                print(f"Thanks for playing. You earned {total_score} points")
                break
            dice_roll = []


if __name__ == "__main__":
    rolls = []

    def mock_roller(num):
        return rolls.pop(0) if rolls else default_roller(num)

    intro()
    play_dice(mock_roller)
