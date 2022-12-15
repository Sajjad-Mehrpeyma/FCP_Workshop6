import sys

def draw_list():
    for row in range(0, 6):
        for column in range(0, 7):
            print(board[row][column], end=" ")
        print()
    sys.exit()

def CheckRowWin():
    player1=0
    player2=0
    for i in range(5, -1,-1):
        for j in range(0, 7):
            if board[i][j]=="r":
                player1+=1
                player2=0
                if player1==4:
                    print("Winner = r")
                    draw_list()
            elif board[i][j]=="y":
                player2+=1
                player1=0
                if player2==4:
                    print("Winner = y")
                    draw_list()

def CheckCollWin():
    player1=0
    player2=0
    for i in range(0,7):
        for j in range(5,-1,-1):
            if board[j][i]=="r":
                player1+=1
                player2=0
                if player1==4:
                    print("Winner = r")
                    draw_list()
            elif board[j][i]=="y":
                player2+=1
                player1=0
                if player2==4:
                    print("Winner = y")
                    draw_list()

def CheckLeftToRight():
    player1=0
    player2=0
    col = 0

    while col<=4:
        for i in range(0,6):
            c = i
            for j in range(col,7):

                if board[c][j]=="r":
                    player1+=1
                    player2=0
                    if player1==4:
                        print("Winner = r")
                        draw_list()
                elif board[c][j]=="y":
                    player2 += 1
                    player1 = 0
                    if player2 == 4:
                        print("Winner = y")
                        draw_list()
                c+=1

                if(c>5):
                    break
        col+=1

def CheckRightTooLeft():
    player1=0
    player2=0
    col = 6

    while col>=4:
        for i in range(6):
            c = i
            for j in range(col,-1,-1):
                if board[c][j]=="r":
                    player1+=1
                    player2=0
                    if player1==4:
                        print("Winner = r")
                        draw_list()
                elif board[c][j]=="y":
                    player2 += 1
                    player1 = 0
                    if player2 == 4:
                        print("Winner = y")
                        draw_list()
                c+=1
                if (c > 5):
                    break

        col-=1


n = int(input())
move_list = [int(x) for x in input().split()]
board = []
for i in range(6):
    col = []
    for j in range(7):
        col.append(0)
    board.append(col)

#board = [
#    ['0', '0', '0', '0', '0', '0', '0', ],
#    ['0', '0', '0', '0', '0', '0', '0', ],
#    ['0', '0', '0', '0', '0', '0', '0', ],
#    ['0', '0', '0', '0', '0', '0', '0', ],
#    ['0', '0', '0', '0', '0', '0', '0', ],
#    ['0', '0', '0', '0', '0', '0', '0', ],
#]

player = 0


for column in move_list:
    for row in range(5,-1,-1):
        if board[row][column-1]==0:
            if player==0:
                board[row][column-1]="r"
                player=1
                break
            else:
                board[row][column-1]="y"
                player=0
                break


CheckRowWin()
CheckCollWin()
CheckLeftToRight()
CheckRightTooLeft()
