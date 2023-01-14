#!/usr/bin/python3
"""RZFeeser | Alta3 Research
Creating a simple dice program utilizing classes."""


# imports from cheadice.py (this is in the local directory)
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice

def main():
    """run-time code"""

    # create two cheater objects
    player_one = Player()
    cheater1 = Cheat_Swapper() # ability is to change 3rd dice roll to 6
    cheater2 = Cheat_Loaded_Dice() # increase all rolls by +1 provided they are < 6

    # each player takes turns
    player_one.roll()
    cheater1.roll()
    cheater2.roll()

    # both cheaters use their cheat methods
    cheater1.cheat()
    cheater2.cheat()

    print(f"Cheater 1 rolled {cheater1.get_dice()}, total: {sum(cheater1.get_dice())} ")
    print(f"Cheater 2 rolled {cheater2.get_dice()}, total: {sum(cheater2.get_dice())} ")
    print(f"Player_one played honestly: {player_one.get_dice()}, total: {sum(player_one.get_dice())} ")
    if sum(cheater1.get_dice()) == sum(cheater2.get_dice()) & sum(cheater2.get_dice()) == sum(player_one.get_dice()):
        print("3 way Draw!")

    elif sum(player_one.get_dice()) > sum(cheater2.get_dice()) & sum(player_one.get_dice()) > sum(cheater1.get_dice()):
        print("honest player 1 wins!")

    elif sum(player_one.get_dice()) < sum(cheater2.get_dice()) & sum(player_one.get_dice()) < sum(cheater1.get_dice()):
        print("one of the cheaters wins!")

    else:
        print("player tied with somone")

if __name__ == "__main__":
    main()
