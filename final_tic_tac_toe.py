x = []
o = []

board = ("1 | 2 | 3 "
         "\n----------"
         "\n4 | 5 | 6 "
         "\n----------"
         "\n7 | 8 | 9"
         "\n")
counter = 0
a = None
b = None


def step_x():
    global counter
    global a
    global board
    global x
    a = input("Player 1, choose where to put x: ")
    if a in board:
        if a == ('x') or a == ('o'):
            print("Please, try again")
            step_x()
        else:
            board = board.replace(a, 'x')
            print (board)
            counter += 1
            x.append(a)

    else:
        print ("Please, try again")
        step_x()


def step_o():
    global counter
    global b
    global board
    global o
    b = input("Player 2, choose where to put o: ")
    if b in board:
        if b == ('x') or b == ('o'):
            print("Please, try again")
            step_o()
        else:
            board = board.replace(b, 'o')
            print (board)
            counter += 1
            o.append(b)

    else:
        print ("Please, try again")
        step_o()


def check_win():
    global x
    global counter
    if (('5' in x) and ('1' in x) and ('9' in x)) or \
       (('3' in x) and ('5' in x) and ('7' in x)) or \
       (('1' in x) and ('2' in x) and ('3' in x)) or \
       (('4' in x) and ('5' in x) and ('6' in x)) or \
       (('7' in x) and ('8' in x) and ('9' in x)) or \
       (('1' in x) and ('4' in x) and ('7' in x)) or \
       (('2' in x) and ('5' in x) and ('6' in x)) or \
       (('3' in x) and ('6' in x) and ('9' in x)):
       print("Player 1 has won")
       counter = 10
    elif (('5' in o) and ('1' in o) and ('9' in o)) or \
       (('3' in o) and ('5' in o) and ('7' in o)) or \
       (('1' in o) and ('2' in o) and ('3' in o)) or \
       (('4' in o) and ('5' in o) and ('6' in o)) or \
       (('7' in o) and ('8' in o) and ('9' in o)) or \
       (('1' in o) and ('4' in o) and ('7' in o)) or \
       (('2' in o) and ('5' in o) and ('6' in o)) or \
       (('3' in o) and ('6' in o) and ('9' in o)):
       print("Player 2 has won")
       counter = 10


while counter < 9:
    print (board)
    step_x()
    check_win()
    if counter > 9:
        break
    if counter == 9:
        print ("Draw!")
        break
    step_o()
    check_win()
    if counter > 9:
        break
    if counter == 9:
        print ("Draw!")
