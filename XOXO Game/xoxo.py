row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input ("Where do you want to put the X? ")

horzional = int(position[0])
veritical = int(position[1])

map[veritical - 1][horzional - 1] = "X"
