from random import randint
from collections import Counter


class GameLogic:

    @staticmethod
    def roll_dice(num_dice):
        """

        param: integer between 1 and 6
        :return: tuple with random values between 1 and 6.
        """
        return tuple(randint(1, 6) for _ in range(0, num_dice))

    @staticmethod
    def calculate_score(roll_tuple):
        """
        param: a tuple of integers that represent a dice roll.
        :return: an integer representing the roll’s score according to rules of game.
        """

        total_score = 0
        counted_dice = Counter(roll_tuple).most_common()

        if not counted_dice:
            return total_score

        # 3, 4, 5, and 6 of a kind
        if (counted_dice[0][1]) >= 3:
            if counted_dice[0][0] != 1:
                total_score += counted_dice[0][0] * 100 * (counted_dice[0][1] - 2)
            else:
                total_score += 1000 * (counted_dice[0][1] - 2)
            counted_dice = counted_dice[1:]

            # Two 3 of a kinds
            if len(counted_dice) == 1 and counted_dice[0][1] == 3:
                if counted_dice[0][0] != 1:
                    total_score += counted_dice[0][0] * 100
                else:
                    total_score += 1000

        # Straight
        if len(counted_dice) == 6:
            total_score += 1500
            return total_score

        # Three Pairs
        if len(counted_dice) == 3 and counted_dice[2][1] == 2:
            total_score += 1500
            return total_score

        # Single 5 or Single 1
        else:
            for dice in counted_dice:
                if dice[0] == 5:
                    total_score += dice[1] * 50
                if dice[0] == 1:
                    total_score += dice[1] * 100

        return total_score

    @staticmethod
    def validate_keepers(nums, keep):
        nums = list(nums)
        keep = list(keep)
        if keep == []:
            return False
        for dice in keep:
            is_there = nums.count(dice)
            if is_there > 0:
                nums.remove(dice)
            else:
                return False
        return True
