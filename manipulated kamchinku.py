MAX_LINES=3
def enter_number_of_lines():
    while True:
        lines=input("ENTER NUMBER OF LINES TO BET ON(1-" + str(MAX_LINES)+")?  ")
        if lines.isdigit():
            lines=int(lines)
            if lines <=MAX_LINES:
                print(lines)
                break
            else:
                print("please enter a valid number of lines")
        else:
            print("please enter a number")
    return lines
enter_number_of_lines()