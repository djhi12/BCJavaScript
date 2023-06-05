# This program should clean up all the balls in any size world. 

"""
 Karel moves up to the next row.
 Precondition Karel is at the start of a just cleaned row.
 Postcondition Karel is at the start of the next row to
 be cleaned, facing east.
"""
def move_up():
    turn_left()
    move()
    turn_right()

"""
 This brings Karel back to the starting position on the row.
 Precondition Karel is at the end of the row, facing a wall.
 Postcondition Karel is at the start of the same row, facing
 east.
"""
def come_back():
    turn_around()
    while front_is_clear():
        move()
    turn_around()

""" 
 This cleans one row of Karel's world.
 Precondition Karel is at first avenue, facing east
 Postcondition Karel is at the end of the street, facing
 east, and all balls in the row have been picked up.
"""
def clean_row():
    while front_is_clear():
        clean_spot()
        move()
    clean_spot()

# This picks up a tennis ball, but only if it is there.
def clean_spot():
    if balls_present():
        take_ball()

while left_is_clear():
    clean_row()
    come_back()
    move_up()
clean_row()
come_back()