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
            print(temp, "is the winner!")
            return True

        temp = self.__checkVerticals()
        if temp != False:
            print(temp, "is the winner!")
            return True

        temp = self.__checkDiagonals()
        if temp != False:
            print(temp, "is the winner!")
            return True

        return False 

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
                return self.__field[0][0]
        #Check right diagonal
        elif self.__field[0][2] == self.__field[1][1] == self.__field[2][0]:
            if self.__field[0][2] != '_' and self.__field[1][1] != '_' and self.__field[2][0] != '_':
                return self.__field[0][0]

        #Diagonal win condition not met
        return False

    def isValid(self, xCord, yCord):
        if self.__field[xCord][yCord] == '_':
            return False
        return True


def playerTurn(myGameField, player):
    while True:
        print("PLAYER", player, "- Input your cordinates <x y>:")
        inputString = input()
        x, y = inputString.split()
        
        #Check for errors...
        if not(int(x) < 3 and int(x) >= 0 and int(y) < 3 and int(y) >= 0):
            print("Your input was out of bounds. Both values must be between 0 and 2.")
        elif myGameField.isValid(int(x), int(y)):
            print("Someone has already played there!")
        else:
            break

    #Place on game field
    myGameField.placeCordinates(player, int(x), int(y))

#Gamefield Object
myGameField = gameField()

#Gameloop (player X always goes first)
while True:
    print("Current game state:")
    myGameField.printField()

    #Player X
    playerTurn(myGameField, 'X')
    print("Current game state:")
    myGameField.printField()

    #Check state
    if myGameField.checkWinConditions(): 
        myGameField.printField()    
        break

    #Player O
    playerTurn(myGameField, 'O')

    #Check state
    if myGameField.checkWinConditions():
        myGameField.printField()
        break  

#Need to do
#   Computer opponent (MINMIXAI)
