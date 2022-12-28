from random import randint
from collections import Counter


class GameLogic:

    @staticmethod
    def roll_dice(num_dice):
        """

        param: integer between 1 and 6
        :return: tuple with random values between 1 and 6.
        """
        return tuple(randint(1, 1) for _ in range(0, num_dice))

    @staticmethod
    def calculate_score(roll_tuple):
        """
        param: a tuple of integers that represent a dice roll.
        :return: an integer representing the roll’s score according to rules of game.
        """

        total_score = 0
        counted_dice = Counter(roll_tuple).most_common()
        print(counted_dice)

        if not counted_dice:
            return total_score

        # 3, 4, 5, and 6 of a kind
        if (counted_dice[0][1]) >= 3:
            if counted_dice[0][0] != 1:
                total_score += counted_dice[0][0] * 100 * (counted_dice[0][1] - 2)
                if counted_dice[0][1] == 6:
                    return total_score
                counted_dice = counted_dice[1:]
                print(counted_dice)
            else:
                total_score += 1000 * (counted_dice[0][1] - 2)
                if counted_dice[0][1] == 6:
                    return total_score
                counted_dice = counted_dice[1:]

            # Two 3 of a kinds
            if len(counted_dice) == 1:
                if counted_dice[0][1] == 3:
                    if counted_dice[0][0] != 1:
                        total_score += counted_dice[0][0] * 100
                        return total_score
                    else:
                        total_score += 1000
                        return total_score

        # Straight
        if len(counted_dice) == 6:
            total_score += 1500
            return total_score

        # Three Pairs
        if len(counted_dice) == 3:
            if counted_dice[2][1] == 2:
                total_score += 1500
                return total_score

        # Single 5 or Single 1
        else:
            for dice in counted_dice:
                if dice[0] == 5:
                    total_score += dice[1] * 50
            for dice in counted_dice:
                if dice[0] == 1:
                    total_score += dice[1] * 100

        print("Total Score", total_score)
        return total_score



