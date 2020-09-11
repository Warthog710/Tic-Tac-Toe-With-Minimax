from tkinter import *
from tkinter import messagebox
import copy

class gameField:
    def __init__(self):
        #Create private 2D List
        self.__field = []
        self.__field.append([])
        self.__field.append([])
        self.__field.append([])

        #Set list to all _s
        for x in range(0, 3):
            for y in range(0,3):
                self.__field[x].append('_')   

    def printField(self):
        for x in range(0,3):
            for y in range(0,3):
                print(self.__field[x][y], end='')
            print("\n")

    def checkWinConditions(self):
        temp = self.__checkHorizontals()
        if temp != False:
            return temp

        temp = self.__checkVerticals()
        if temp != False:
            return temp

        temp = self.__checkDiagonals()
        if temp != False:
            return temp

        #Check for tie condition
        for x in range(0,3):
            for y in range(0,3):
                if self.isValid(x,y):
                    return False

        return 'T' 

    def placeCordinates(self, player, xCord, yCord):
        if player == 'X':
            self.__field[xCord][yCord] = 'X'
        else:
            self.__field[xCord][yCord] = 'O'


    #Private helper method
    def __checkHorizontals(self):
        for x in range(0,3):
            if self.__field[x][0] == self.__field[x][1] == self.__field[x][2]:
                #Return win char if no _ are present
                if self.__field[x][0] != '_' and self.__field[x][1] != '_' and self.__field[x][2] != '_':
                    return self.__field[x][0]
        return False

    #Private helper method
    def __checkVerticals(self):
        for x in range(0,3):
            if self.__field[0][x] == self.__field[1][x] == self.__field[2][x]:
                #Return win char if no _ are present
                if self.__field[0][x] != '_' and self.__field[1][x] != '_' and self.__field[2][x] != '_':
                    return self.__field[0][x]
        return False

    #Private helper method
    def __checkDiagonals(self):
        #Check left diagonal
        if self.__field[0][0] == self.__field[1][1] == self.__field[2][2]:
            if self.__field[0][0] != '_' and self.__field[1][1] != '_' and self.__field[2][2] != '_':
                return self.__field[1][1]
        #Check right diagonal
        elif self.__field[0][2] == self.__field[1][1] == self.__field[2][0]:
            if self.__field[0][2] != '_' and self.__field[1][1] != '_' and self.__field[2][0] != '_':
                return self.__field[1][1]

        #Diagonal win condition not met
        return False

    def isValid(self, xCord, yCord):
        if self.__field[xCord][yCord] == '_':
            return True
        return False 

    def clearField(self):
        for x in range(0, 3):
            for y in range(0,3):
                self.__field[x][y] = '_'


class cordinates:
    x = 0
    y = 0

def computerTurn(myGameField, player):
    cords = cordinates()
    maxEval = -100
    alpha = -100
    beta = 100
    maximizer = False
    depth = 5

    #Iterate through all possible moves...
    for x in range(0,3):
        for y in range(0,3):
            if myGameField.isValid(x,y):
                    temp = copy.deepcopy(myGameField)
                    temp.placeCordinates('X', x, y)
                    evaluation = minimax(temp, depth, maximizer, alpha, beta)
                    if maxEval < evaluation:
                        cords.x = x
                        cords.y = y
                        maxEval = evaluation
    
    #print("Max Score:", maxEval)
    #print("Rec:", cords.x, cords.y)
    return cords

def minimax(myGameField, depth, maximizingPlayer, alpha, beta):
    #If win condition has been met or depth is zero
    #Return the score Win = 1, lose = -1, otherwise zero
    if myGameField.checkWinConditions() or depth == 0:
        if myGameField.checkWinConditions() == 'X':
            return 1
        elif myGameField.checkWinConditions() == 'O':
            return -1
        else:
            return 0

    #If I am trying to maximize the player...
    if maximizingPlayer:
        maxEval = -100
        for x in range(0,3):
            for y in range(0,3):
                if myGameField.isValid(x, y):
                    temp = copy.deepcopy(myGameField)
                    temp.placeCordinates('X', x, y)
                    evaluation = minimax(temp, depth -1, False, alpha, beta)
                    maxEval = max(maxEval, evaluation)
                    alpha = max(alpha, evaluation)
                    if beta <= alpha:
                        break
        return maxEval

    #Else, I must be minimizing the player
    else:
        minEval = 100
        for x in range(0,3):
            for y in range(0,3):
                if myGameField.isValid(x,y):
                    temp = copy.deepcopy(myGameField)
                    temp.placeCordinates('O', x, y)
                    evaluation = minimax(temp, depth - 1, True, alpha, beta)
                    minEval = min(minEval, evaluation)
                    beta = min(beta, evaluation)
                    if beta <= alpha:
                        break
        return minEval

def resetGame():
    myGameField.clearField()
    button0['image'] = emptyImage
    button0['state'] = ACTIVE
    button1['image'] = emptyImage
    button1['state'] = ACTIVE
    button2['image'] = emptyImage
    button2['state'] = ACTIVE
    button3['image'] = emptyImage
    button3['state'] = ACTIVE
    button4['image'] = emptyImage
    button4['state'] = ACTIVE
    button5['image'] = emptyImage
    button5['state'] = ACTIVE
    button6['image'] = emptyImage
    button6['state'] = ACTIVE
    button7['image'] = emptyImage
    button7['state'] = ACTIVE
    button8['image'] = emptyImage
    button8['state'] = ACTIVE

def whoWon(winValue):

    if winValue == 'X':
        if human == 'X':
            if messagebox.askyesno(title="Somebody won...", message='O won the game! Do you want to play again?'):
                resetGame()
                whoFirst()
            else:
                root.destroy()                
        else:
            if messagebox.askyesno(title="Somebody won...", message='X won the game! Do you want to play again?'):
                resetGame()
                whoFirst()
            else:
                root.destroy()   

    elif winValue == 'O':
        if human == 'X':
            if messagebox.askyesno(title="Somebody won...", message='X won the game! Do you want to play again?'):
                resetGame()
                whoFirst()
            else:
                root.destroy()  
        else:
            if messagebox.askyesno(title="Somebody won...", message='O won the game! Do you want to play again?'):
                resetGame()
            else:
                root.destroy()  
    
    else:
        if messagebox.askyesno(title="A tie???", message='Tie! Do you want to play again?'):
            resetGame()
            whoFirst()
        else:
            root.destroy()

def turn(buttonIndex):
    #Human turn
    if buttonIndex == 0:
        if human == 'X':
            button0['image'] = imageX
        else:
            button0['image'] = imageO

        button0['state'] = DISABLED
        myGameField.placeCordinates('O', 0, 0)
    elif buttonIndex == 1:
        if human == 'X':
            button1['image'] = imageX
        else:
            button1['image'] = imageO
           
        button1['state'] = DISABLED
        myGameField.placeCordinates('O', 0, 1)
    elif buttonIndex == 2:
        if human == 'X':
            button2['image'] = imageX
        else:
            button2['image'] = imageO
           
        button2['state'] = DISABLED
        myGameField.placeCordinates('O', 0, 2)
    elif buttonIndex == 3:
        if human == 'X':
            button3['image'] = imageX
        else:
            button3['image'] = imageO
           
        button3['state'] = DISABLED
        myGameField.placeCordinates('O', 1, 0)
    elif buttonIndex == 4:
        if human == 'X':
            button4['image'] = imageX
        else:
            button4['image'] = imageO
           
        button4['state'] = DISABLED
        myGameField.placeCordinates('O', 1, 1)
    elif buttonIndex == 5:
        if human == 'X':
            button5['image'] = imageX
        else:
            button5['image'] = imageO
           
        button5['state'] = DISABLED
        myGameField.placeCordinates('O', 1, 2)
    elif buttonIndex == 6:
        if human == 'X':
            button6['image'] = imageX
        else:
            button6['image'] = imageO
           
        button6['state'] = DISABLED
        myGameField.placeCordinates('O', 2, 0)
    elif buttonIndex == 7:
        if human == 'X':
            button7['image'] = imageX
        else:
            button7['image'] = imageO
           
        button7['state'] = DISABLED
        myGameField.placeCordinates('O', 2, 1)
    else:
        if human == 'X':
            button8['image'] = imageX
        else:
            button8['image'] = imageO
           
        button8['state'] = DISABLED
        myGameField.placeCordinates('O', 2, 2)

    myGameField.printField()
    temp = myGameField.checkWinConditions()
    if temp: 
        whoWon(temp)
        return

    #Computer turn
    cTurn()

def cTurn():
    cords = computerTurn(myGameField, 'X')
    myGameField.placeCordinates('X', cords.x, cords.y)
    
    if cords.x == 0 and cords.y == 0:
        if computer == 'X':
            button0['image'] = imageX
        else:
            button0['image'] = imageO

        button0['state'] = DISABLED
    elif cords.x == 0 and cords.y == 1:
        if computer == 'X':
            button1['image'] = imageX
        else:
            button1['image'] = imageO

        button1['state'] = DISABLED
    elif cords.x == 0 and cords.y == 2:
        if computer == 'X':
            button2['image'] = imageX
        else:
            button2['image'] = imageO

        button2['state'] = DISABLED
    elif cords.x == 1 and cords.y == 0:
        if computer == 'X':
            button3['image'] = imageX
        else:
            button3['image'] = imageO
            
        button3['state'] = DISABLED
    elif cords.x == 1 and cords.y == 1:
        if computer == 'X':
            button4['image'] = imageX
        else:
            button4['image'] = imageO

        button4['state'] = DISABLED
    elif cords.x == 1 and cords.y == 2:
        if computer == 'X':
            button5['image'] = imageX
        else:
            button5['image'] = imageO

        button5['state'] = DISABLED
    elif cords.x == 2 and cords.y == 0:
        if computer == 'X':
            button6['image'] = imageX
        else:
            button6['image'] = imageO

        button6['state'] = DISABLED
    elif cords.x == 2 and cords.y == 1:
        if computer == 'X':
            button7['image'] = imageX
        else:
            button7['image'] = imageO

        button7['state'] = DISABLED
    else:
        if computer == 'X':
            button8['image'] = imageX
        else:
            button8['image'] = imageO

        button8['state'] = DISABLED

    myGameField.printField()
    temp = myGameField.checkWinConditions()
    if temp: 
        whoWon(temp)
        return
    

def whoFirst():
    global human
    global computer

    if messagebox.askyesno(title="Who goes first?", message="Do you want the computer to go first?"):
        human = 'O'
        computer = 'X'  
        cTurn()
    else:
        human = 'X'
        computer = 'O'    

#EXECUTION STARTS HERE
root = Tk()

root.title("Tic-Tac-Toe")
root.geometry("320x320")
root.resizable(0,0)

imageX = PhotoImage(file="images/x.png")
imageO = PhotoImage(file="images/o.png")
emptyImage = PhotoImage(file="images/empty.png")
myGameField = gameField()
human = 'O'
computer = 'X'


#Create the buttons
button0 = Button(root, image=emptyImage, command=lambda: turn(0))
button1 = Button(root, image=emptyImage, command=lambda: turn(1))
button2 = Button(root, image=emptyImage, command=lambda: turn(2))
button3 = Button(root, image=emptyImage, command=lambda: turn(3))
button4 = Button(root, image=emptyImage, command=lambda: turn(4))
button5 = Button(root, image=emptyImage, command=lambda: turn(5))
button6 = Button(root, image=emptyImage, command=lambda: turn(6))
button7 = Button(root, image=emptyImage, command=lambda: turn(7))
button8 = Button(root, image=emptyImage, command=lambda: turn(8))

#Setup the buttons
button0.grid(column=0,row=0)
button1.grid(column=1,row=0)
button2.grid(column=2,row=0)
button3.grid(column=0,row=1)
button4.grid(column=1,row=1)
button5.grid(column=2,row=1)
button6.grid(column=0,row=2)
button7.grid(column=1,row=2)
button8.grid(column=2,row=2)

#Call the starter function
whoFirst()
root.mainloop()
