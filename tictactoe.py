winConditionMet = "none"
winType = "none"
rows = list()
thisstr = "-"
numcols = 0
# explain the game
print("This tictactoe analyzer is a little unusual. \nYou enter the values of your tictactoe grid one row at a time,\n"
      "but it doesn't have to be for a 3 X 3 grid. \nThe grid can be any size and does not have to have the same"
      "number of rows as columns. \nIf you don't have a symmetrical grid, diagonals will not be checked.\n"
      "When you want to stop entering rows, just hit the enter on a blank line.")
# get each row of the tictactoe board as a string. If the string is empty, stop asking for input
while thisstr != "":
    thisstr = input("Enter a row (x, o, or -): ")
    if len(rows) == 0:
        numcols = len(thisstr)
    if thisstr == "":
        break
    # normalize the length of rows to match the first row
    if len(thisstr) > numcols:
        thisstr = thisstr[0:numcols]
    else:
        thisstr = thisstr + "-"*(numcols-len(thisstr))
    # print("numcols = {0}, thisstr = {1}".format(numcols, thisstr))
    thisrow = list(thisstr)
    for i in thisrow:
        if i not in "xo-":
            print("You entered an incorrect value.")
            break
        else:
            rows.append(thisrow)

# print(rows)
# print("Grid size = {}".format(numcols))

# check for horizontal win conditions
# print("Check horizontals")
size = len(rows)
if size == 0:
    print("You didn't enter any rows. Please start again.")
    exit(0)
for currRow in rows:
    marker = currRow[0]
    if marker == "-":
        continue
    for i in range(1, len(currRow)):
        if currRow[i] != marker:
            break
    else:
        winConditionMet = marker
        winType = "horizontal"
        break

# check for vertical win conditions
if winConditionMet == "none":
    # print("Checking verticals")
    rowsize = len(rows[0])
    for col in range(0, rowsize):
        marker = rows[0][col]
        if marker == "-":
            continue
        for row in range(1, size):
            if rows[row][col] != marker:
                break
        else:
            winConditionMet = marker
            winType = "vertical"
            break

# check for length of rows versus number of rows
if winConditionMet == "none":
    # no winner yet
    if size != numcols:
        print("You do not have the same number of rows as columns. Diagonals will not be checked.")
    else:
        # print("Checking first diagonal")
        marker = rows[0][0]
        if marker != "-":
            for i in range(1, size):
                if rows[i][i] != marker:
                    break
            else:
                winConditionMet = marker
                winType = "first diagonal"

if winConditionMet == "none":   # still no winner
    # print("numcols = {}".format(numcols))
    marker = rows[0][numcols-1]
    if marker != "-":
        # print("Checking second diagonal, marker is {}".format(marker))
        for i in range(1, size):
            # print("i is {0}, (numcols-1)-i is {1}, value is {2}".format(i, (numcols-1)-i, rows[i][(numcols-1)-i]))
            if rows[i][(numcols-1)-i] != marker:
                break
        else:
            winConditionMet = marker
            winType = "second diagonal"

print("Win condition: {0} and win type: {1}".format(winConditionMet, winType))


