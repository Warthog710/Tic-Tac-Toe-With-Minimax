import copy

class gameField:
    def __init__(self):
        #Create private 2D List
        self.__field = []
        self.__field.append([])
        self.__field.append([])
        self.__field.append([])

        #Set list to all 0s
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

class cordinates:
    x = 0
    y = 0

def playerTurn(myGameField, player):
    while True:
        print("PLAYER", player, "- Input your cordinates <x y>:")
        inputString = input()
        x, y = inputString.split()
        
        #Check for errors...
        if not(int(x) < 3 and int(x) >= 0 and int(y) < 3 and int(y) >= 0):
            print("Your input was out of bounds. Both values must be between 0 and 2.")
        elif not(myGameField.isValid(int(x), int(y))):
            print("Someone has already played there!")
        else:
            break

    #Place on game field
    myGameField.placeCordinates(player, int(x), int(y))

def computerTurn(myGameField, player):
    cords = cordinates()
    maxEval = -100

    #Iterate through all possible moves...
    for x in range(0,3):
        for y in range(0,3):
            if myGameField.isValid(x,y):
                    temp = copy.deepcopy(myGameField)
                    temp.placeCordinates('X', x, y)
                    evaluation = minimax(temp, 3, False)
                    if maxEval < evaluation:
                        cords.x = x
                        cords.y = y
                        maxEval = evaluation
    
    return cords

def minimax(myGameField, depth, maximizingPlayer):
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
                    evaluation = minimax(temp, depth -1, False)
                    maxEval = max(maxEval, evaluation)
        return maxEval

    #Else, I must be minimizing the player
    else:
        minEval = 100
        for x in range(0,3):
            for y in range(0,3):
                if myGameField.isValid(x,y):
                    temp = copy.deepcopy(myGameField)
                    temp.placeCordinates('O', x, y)
                    evaluation = minimax(temp, depth - 1, True)
                    minEval = min(minEval, evaluation)
        return minEval

def whoWon(winValue):
    if winValue == 'X':
        print("X won the game!")

    elif winValue == 'O':
        print("O won the game!")
    
    else:
        print("Tie!")

def playGame(myGameField):
    #Gameloop (player X always goes first)
    while True:        
        #Player X (computer)
        cords = computerTurn(myGameField, 'X')
        myGameField.placeCordinates('X', cords.x, cords.y)
        print("Current game state:")
        myGameField.printField()

        #Check state
        temp = myGameField.checkWinConditions()
        if temp: 
            whoWon(temp)
            myGameField.printField()
            break

        #Player O (human)
        playerTurn(myGameField, 'O')

        #Check state
        temp = myGameField.checkWinConditions()
        if temp: 
            whoWon(temp)
            myGameField.printField()
            break

#EXECUTION STARTS HERE!!!      
    
myGameField = gameField()
playGame(myGameField)

#Need to do
#   Add GUI (Tkinter?)
