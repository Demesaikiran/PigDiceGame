import random
from pynput.keyboard import Key, Listener


dice = [1, 2, 3, 4, 5, 6]
position = 0
prev = []
diceCounts = 0
OnesCount = 0


def press(key):
    global position, prev, dice, diceCounts, OnesCount

    if key == Key.enter:

        dice_value = random.choice(dice)

        diceCounts += 1
        if dice_value != 1:
            prev.append(dice_value)
            position += dice_value
            print("\nThe Dice value is {0}".format(dice_value))
            print("Your position is {0}\n".format(position))
        else:
            OnesCount += 1
            print("\nThe Dice value is 1...\n")
            if not prev:
                position = 0
            else:
                position -= prev[-1]
                print("Your prev value is {0}".format(prev.pop()))

                if position < 0:
                    position = 0
            print("Your position is {0}\n".format(position))
        if position >= 100:
            print("-----------------------------------------\nNumber of times you rolled the dice = {0}\nNumber of Ones you got = {1}".format(diceCounts, OnesCount))
            exit(0)

    else:
        print("Enter correct key")


def release(key):
    print("--------------------------------------------")
    print("Press the button <Enter> to roll the dice: ", end='')
    if key == Key.esc:
        return False


with Listener(on_press=press, on_release=release) as Listener:
    print("The PIG_DICE game is started...\n")
    print("Press the button <Enter> to roll the dice: ", end='')
    Listener.join()