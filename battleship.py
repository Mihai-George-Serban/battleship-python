

# def initialize_board():
    

def generate_board():
    global inputu_userului
    inputu_userului = input("Cat de mare sa fie bordul?")
    if int(inputu_userului) in range(5, 11):
        board = [[0 for i in range(int(inputu_userului))] for j in range(int(inputu_userului))]
        value = 0
        global myDict
        myDict = {

        }
        while value in range(0, int(inputu_userului)):
                myDict[(chr(65 + value))] = board[value]
                value = value + 1
        return myDict
    else:
        print("Bordul trebuie sa fie intre 5x5 - 10x10")
        generate_board()
    
def get_coord():
    # myDict = {'A': [1, 2, 3, 4, 5, 6], 'B': [0, 0, 0, 0, 0, 0], 'C': [0, 0, 0, 0, 0, 0], 'D': [0, 0, 0, 0, 0, 0], 'E': [0, 0, 0, 0, 0, 0], 'F': [0, 0, 0, 0, 0, 0]}
    # print(myDict)
    ship = "X"
    row = input("Linia? ")
    coloana = input("Coloana? ")
    if row in myDict.keys():
        myDict[row][(int(coloana) - 1)] = ship
        directie = input("Ce directie vrei? ")
        temp = iter(myDict)
        # if directie == "jos" or "sud" or "S":
        #     for key in temp:
        #         if key == row:
        #             south = next(temp, None)
        #             myDict[south][(int(coloana) - 1)] = ship
        if directie == "sus" or "nord" or "N":
            for key in sorted(temp, reverse=True):
                if key == row:
                    north = next(temp, None)
                    myDict[north][(int(coloana) - 1)] = ship
    build_board()

        
# No. Class of ship 	Size
# 1 	Carrier 	    5
# 2 	Battleship 	    4
# 3 	Cruiser 	    3
# 4 	Submarine 	    3
# 5 	Destroyer 	    2 

# def place_ship():
#     ship="x"
#      = ship


def build_board():
    list_of_numbers = []
    for i in range(0, (int(inputu_userului) + 1)):
        list_of_numbers.append(i)
        b = str(str(list_of_numbers).strip("[]"))
    text = b.replace(",", " ")
    print("")
    print("\u0332".join(text).replace("0", ""))
    for row in myDict:
        a = str(myDict[row]).replace("'", "")
        replaced_a = a.replace(",", " ")
        print(str(row) + " |" + replaced_a.strip("[]"))
    print("")


def main():
    generate_board()
    build_board()
    get_coord()


main()

