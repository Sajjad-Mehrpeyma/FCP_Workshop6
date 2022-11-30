n = int(input())
move_list = []
move_list = (input().split(" "))
board = []
for i in move_list:
    board.append(int(i))

sample_list = [
    ['0', '0', '0', '0', '0', '0', '0', ],
    ['0', '0', '0', '0', '0', '0', '0', ],
    ['0', '0', '0', '0', '0', '0', '0', ],
    ['0', '0', '0', '0', '0', '0', '0', ],
    ['0', '0', '0', '0', '0', '0', '0', ],
    ['0', '0', '0', '0', '0', '0', '0', ],
]


def draw_list(list):
    for list1 in list:
        for item in list1:
            print(item, end=" ")
        print()


def move(list, column, color):
    for row in range(5, -1, -1):
        if list[row][column-1] == "0":
            list[row][column-1] = color
            break


counter = 0
for column in board:
    if counter % 2 == 0:
        player = "r"
        move(sample_list, column, player)

    else:
        player = "y"
        move(sample_list, column, player)
    counter += 1

# winner is recognized by number of moves
if len(board) % 2 == 1:
    winner = "r"

if len(board) % 2 == 0:
    winner = "y"

print("Winner = ", winner)
draw_list(sample_list)
