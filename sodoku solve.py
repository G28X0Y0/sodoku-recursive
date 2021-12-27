from time import perf_counter


#PLAYING FIELD
#I HAVE IT INPUT THIS WAY TO MAKE IT EASIER TO WORK WITH. 
board = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

#CHECK IS BOARD IS EVEN VALID
def valid(bo, num, pos): #WE ARE GOING TO NEED THE BOARD, NUMBER, AND POSITION

    #CHECK ROW
    for i in range(len(bo[0])):  #GRAB RANGE FROM BOARD INDEX
        if bo[pos[0]] [i] == 9 and pos[1] != i: 
            return False

    #CHECK COLLUM
    for i in range(len(bo)):
        if bo[i] [pos[1]] == 9 and pos[0] != i:
            return False

    #CHECK BOX
    box_x = pos[1] // 3
    box_y = pos[0] // 3

#TAKE PLAYING FIELD AND PRINT IT OUT IN CLASSIC SODOKU LAYOUT
def print_board(bo):


    for i in range(len(bo)):   #TAKE INDEXES OF BOARD AND TURN THEM INTO VALUES
        if i % 3 == 0 and i != 0: #TAKE EVERY 3RD ROW 
            print("--------------------------------") #PRINT HORIZONTAL LINE UNDERNEATH
        
        for j in range(len(bo[0])): #TAKE INDEXED ROW AND LOOK INSIDE LIST FOR ROW 
            if j % 3 == 0 and j != 0: #TAKE EVERY 3RD INDEX POSITION IN INDIVIDUAL LIST
                print(" | ", end=" ") #PRINT VERTRICAL LINE AT EVERY 3RD ROW
            
            if j == 8:
                print(bo[i] [j]) #AT POSITION 8 JUST PRINT THE NUMBER SINCE IT'S THE END OF THE ROW
            
            else:
                print(str(bo[i][j]) + " ", end=" ") #IF POSITION IN ROW OR COLLUM ISN'T ON A 3RD OR IF IT ISN'T THE END, JUST PRINT NUMBER WITH SPACES ON EITHER SIDEL


#FIND EMPTY CELLS. CODE IS SELF EXPLAINATORY.
def find_empty(bo):
    for i in range(len(bo)): 
        for j in range(len(bo[0])):
            if bo[i][j] == 0: 
                return (i, j) #ROW AND COLLUM

