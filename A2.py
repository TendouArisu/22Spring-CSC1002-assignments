import turtle
import random

g_block_set1 = []                           # store initial 5*5 array color in number form  
g_block_set2 = []                           # store each color of squares in str form, to change and search pencolor easier              
g_click_set1 = []                           # store info about the nearest clicked square turtles
g_click_set2 = []                           # store the number of the nearest clicked square turtles, easier to operate in next code
g_squares = locals()                        # to create 25 square turtles
g_forward_number = 0                        # to draw the squares in a row one by one
g_initial = 1                               # a initial number to create 25 square turtle by whlie logic
g_row = -1                                  # This is row of squares, to better draw on screen
g_column = 0                                # This is row of squares, to better draw on screen

def click(x, y):
    '''
    This function is to detect the position of mouse1 click.
    And it will react to user correspondingly.
    All the color flipping operations are running in this function. 
    '''                                        
    if y < -250:                                                        # user click color set under 5*5 array

        position = round((x+50)/100) + 2                                # find which color was clicked in color set and store in b
        posi = {0:'red', 1:'orange', 2:'yellow', 3:'blue', 4:'green'}
        b = posi[position]

        if g_click_set1 != []:

            click_set3 = []                                             # a intermediary list to contain what squares color should be changed in one filp
            click_set3.append(g_click_set2[0][0])
            sub = 0                                                     # a local variable to calculate times

            while sub < len(click_set3):                                # detect the suquare whose color are same to initial one

                if (
                    (click_set3[sub]-1)%5 != 0 and
                    (click_set3[sub]-1) not in click_set3 and
                    g_block_set2[click_set3[sub]-2] == g_block_set2[g_click_set2[0][0]-1]
                    ):
                    p = click_set3[sub] - 1
                    click_set3.append(p)                                # left square of initial one

                if (
                    (click_set3[sub]+1)%5 != 1 and
                    (click_set3[sub]+1) not in click_set3 and
                    g_block_set2[click_set3[sub]] == g_block_set2[g_click_set2[0][0]-1]
                    ):
                    p = click_set3[sub] + 1
                    click_set3.append(p)                                # right square of initial one

                if (
                    click_set3[sub]+5 < 26 and
                    (click_set3[sub]+5) not in click_set3 and
                    g_block_set2[click_set3[sub]+4] == g_block_set2[g_click_set2[0][0]-1]
                    ):
                    p = click_set3[sub] + 5
                    click_set3.append(p)                                # upper square of initial one

                if (
                    click_set3[sub]-5 > 0 and
                    (click_set3[sub]-5) not in click_set3 and
                    g_block_set2[click_set3[sub]-6] == g_block_set2[g_click_set2[0][0]-1]
                    ): 
                    p = click_set3[sub]-5
                    click_set3.append(p)                                # lower square of initial one

                sub += 1

            for ii in click_set3:
                exec("x"+f'{ii}'+".fillcolor(b)")                       # change color
                g_block_set2[ii-1] = b

            exec(f'{g_click_set1[0]}'+".pencolor('white')")
            del g_click_set1[0]                                         # reset settings
            del g_click_set2[0]
            turtle.update()      
            click_set3 = []

    else:                                                               # user click 5*5 array

        if g_click_set1 != []:
            exec(f'{g_click_set1[0]}'+".pencolor('white')")
            del g_click_set1[0]                                         # delete former highlight square
            del g_click_set2[0]
            turtle.update()

        x, y = round(x/100)+2, round(y/100)+2
        exec("x"+f'{y*5+x+1}'+".pencolor('black')")                     # highlight the nearest clicked square
        g_click_set1.append("x"+f'{y*5+x+1}')
        g_click_set2.append([y*5+x+1])
        turtle.update()

def block_color(x, y):
    '''
    This function is to help to create 5*5 initial array and their colors.
    '''
    c = g_block_set1[x][y]                                              # store color in c
    colorlist = {0:'red', 1:'orange', 2:'yellow', 3:'blue', 4:'green'}
    return colorlist[c]

def main_game(initial, row, column, forward_number):
    '''
    This function is to create all the initial graph before interacting with user.
    '''
    turtle.tracer(0)
    turtle.title('Color Flipping')
    turtle.setup(width=1500, height=1000, startx=200, starty=0)

    for jj in range(5):                                                      # create 5*5 color set in number, for easier use
        subset=[]
        for jj in range(5):
            subset.append(random.randint(0, 4))
        g_block_set1.append(subset[:])

    while initial <= 25:                                                     # create 5*5 array board

        if initial%5 == 1:                                                   # change row and column
            row += 1
            column -= 5

        g_squares['x'+str(initial)] = turtle.Turtle()
        g_squares['x'+str(initial)].penup()
        g_squares['x'+str(initial)].pen(outline=8, fillcolor=block_color(row,column), pencolor='white')
        g_squares['x'+str(initial)].goto(-200, -200+100*row)
        g_squares['x'+str(initial)].shape('square')
        g_squares['x'+str(initial)].shapesize(4, 4)
        g_squares['x'+str(initial)].fd(forward_number-500*row)
        g_block_set2.append(g_squares['x'+str(initial)].color()[1])
        forward_number = forward_number + 100
        g_squares['x'+str(initial)].onclick(click)
        initial += 1
        column += 1

    for k in range(26, 31):                                                  # create color set under 5*5 array
        
        underset = {26:'red', 27:'orange', 28:'yellow', 29:'blue', 30:'green'}
        e = underset[k]
        g_squares['x'+str(k)] = turtle.Turtle()
        g_squares['x'+str(k)].penup()
        g_squares['x'+str(k)].pen(outline=8, fillcolor=e, pencolor='black')
        g_squares['x'+str(k)].shape('square')
        g_squares['x'+str(k)].shapesize(4, 4)
        g_squares['x'+str(k)].goto(-250, -300)
        g_squares['x'+str(k)].fd((k-26)*100)
        g_squares['x'+str(k)].onclick(click)

    turtle.update()
    turtle.mainloop()

if __name__ == '__main__':
    main_game(g_initial, g_row, g_column, g_forward_number)