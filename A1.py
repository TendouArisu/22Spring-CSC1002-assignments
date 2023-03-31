import random

count = 1                        # How many times the user guesses
num = 0                          # How many balls the user choose to play
heavy_ball = 0                   # The id of the odd-ball(the program randomly selects)

def circular_guess(num, heavy_ball):
    """
    This function is to let the user use scale to guess the odd ball id.
    The fuction will circularly run if the guess is wrong.
    Because this part need a extra circulation and to let the whole code structure more clear,
    I write them in a function.
    """
    global count
    while True:

        print("""\n\tYou are prompted to enter the balls
        to be placed on the pans of the scale,
        seperate each ball identifier with one minimum space,
        e.g. 1 2 3\n""")

        left_balls, right_balls = check_plane(num)                       # get elements of both scale sides
        print('The scale shows: ',end="")
        if str(heavy_ball) in left_balls:
            print("Left pan is down")
        elif str(heavy_ball) in right_balls:
            print("right pan is down")
        else:
            print('equal')

        print('Enter the odd ball number you guess:')
        answer = get_int()                                                # user's guess
        if answer == heavy_ball:
            print(f"""\tCongratulations!!! You are right!!!
            Scale usage count:{count}""")
            count = 1                                                     # reset the counts when user is right
            break
        else:
            print('Sorry you are wrong, go ahead, remember to input valid number')
            count = count + 1                                             # count how many times user guesses

def main_game():
    """
    This function is the main body of the game.
    """
    while True:

        print("""\tWelcome to odd-ball game! You will choose an even number of balls.
        They are labelled and among them one is heavier, which called odd ball.
        You need to find the odd ball with a weighing scale
        \n\tEnjoy the game!\n\n""")

        print("Enter the number of balls for the game", end="")
        num = get_even_int()                                                     # ball numbers
        heavy_ball = random.randint(1, num)                                      # odd ball number

        circular_guess(num, heavy_ball)                                           

        print('Do you want to play again? If yes, please type:y If no, please type n')
        again = get_yes_or_no()                                                  # judge whether the game will continue
        if again == 'n':
            break

def check_plane(num):
    """
    This fuction is to get and check the inputs on both scale sides whether is valid or not.
    And it will return two lists of elements of scale both sides.
    The Invalid inputs include:
    1. something aren't numbers or spaces
    2. demicals and negative numbers
    3. duplicate inputs
    4. the input id isn't between 1 and the last id of the balls
    5. element number are not equal
    6. empty inputs
    """
    while True:

        whether_correct_or_not = 1                                               # set a previous value to judge whether input is valid
        l = input("Enter the balls you want to place on left pan:")              # save the user's original inputs
        r = input("Enter the balls you want to place on right pan:")
        left_balls = l.split()
        right_balls = r.split()
        
        if left_balls == [] or right_balls == []:                                # Invalid case 6
            whether_correct_or_not = 0

        if len(left_balls) != len(right_balls):                                  # Invaild case 5
            whether_correct_or_not = 0

        for element in left_balls:                                               # Invalid case 1, 2, and 4
            try:
                element = int(element)
                if element > num or element < 1 :
                    whether_correct_or_not = 0
            except:
                whether_correct_or_not = 0

        for element in right_balls:
            try:
                element = int(element)
                if element > num or element < 1 :
                    whether_correct_or_not = 0
            except: whether_correct_or_not = 0

        mid = left_balls + right_balls                                           # Invalid case 3
        mid = set(mid)                                                           # delete the duplicate elements
        if len(mid) < (len(left_balls) + len(right_balls)):
            whether_correct_or_not = 0

        if whether_correct_or_not == 1:
            break
        else: print(f"""\n\tYour inputs for left:{l}, right:{r}\n\n\tInvalid input!
        \n\tPlease ensure correct ball identifiers (1-{num})
        are entered on each pan, no idenyical ball on one side or both sides
        both pans should have the same number of balls and must have at least one ball\n""")

    return left_balls, right_balls

def get_int():
    """
    This function is to get a int input.
    Other inputs are invaild.
    """
    while True:

        num1 = input()
        try:
            num1 = int(num1)                                                      # ensure input is a int
            if num1 > 0:
                break
            else: 
                print("Invaild inputs!\nPlease input a positive intergar", end="")
        except: print("Invaild inputs!\nPlease input a positive intergar", end="")

    return num1

def get_yes_or_no():
    """
    This function is to get whether player wants to play again or not.
    Other inputs are invaild.
    """
    while True:

        num1 = input()
        if num1 == 'y' or num1 == 'n':
            break
        else:
            print("Invaild inputs!\nPlease input y or n", end="")

    return num1

def get_even_int():
    """
    This function is to get an even number as the balls numbers.
    Other inputs are invalid.
    """
    while True:

        num1 = input()
        try:
            num1 = int(num1)
            if num1 % 2 == 0 and num1 > 0:                                         # ensure input is an even int
                break
            else:
                print("Invaild inputs!\nPlease input a positive even intergar", end="")
        except: print("Invaild inputs!\nPlease input a positive even intergar", end="")

    return num1
if __name__ == '__main__':
    main_game()