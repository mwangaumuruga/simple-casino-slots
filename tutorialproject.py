import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbol_count={
            "A":8,
            "B":8,
            "C":8,
            "D":8
           }
symbol_value={
            "A":5,
            "B":4,
            "C":3,
            "D":2
           }
def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range (lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
             break
            else:
                winnings+=values[symbol]*bet
                winning_lines.append(line +1)
    return winnings,winning_lines


 
def get_slot_machine(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns=[]
    for _ in range(cols):
        column=[]
        for _ in range(rows):
            current_symbols=all_symbols[:]
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machines(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate (columns):
            if i != len(columns) -1:
              print(column [row],end = " | ")
            else:
              print(column [row],end="")
        print()





def deposit():
    while True:
        amount=input("ENTER AMOUNT YOU WANNA DEPOSIT IN YOUR ACCOUNT  $")
        if amount.isdigit():
            amount=int(amount)
            if amount >0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("please enter a number")
    return amount

def enter_number_of_lines():
    while True:
        lines=input("ENTER NUMBER OF LINES TO BET ON(1-" + str(MAX_LINES)+")?  ")
        if lines.isdigit():
            lines=int(lines)
            if lines <= MAX_LINES:
                break
            else:
                print("please enter a valid number of lines")
        else:
            print("please enter a number")
    return lines

def get_bet():
    while True:
        amount=input("ENTER AMOUNT YOU WANNA STAKE ON EACH LINE  $")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET <=amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between  ${MIN_BET} & ${MAX_BET}")
        else:
            print("please enter a number")
    return amount


def spin(balance):
     lines=enter_number_of_lines()
    
     while True:
      bet=get_bet()
      total=bet*lines
      if total>balance:
         print(f"YOU CAN NOT BET ON THAT AMOUNT.YOUR ACCOUNT  BALANCE IS $ {balance}")
      else:
         break
      
    
     print(f"YOU ARE BETTING {bet} DOLLARS  ON {lines} lines.THE TOTAL BET COST IS {total}")

     slot=get_slot_machine(ROWS,COLS, symbol_count)
     print_slot_machines(slot)
     winnings,winning_lines=check_winnings(slot, lines, bet,symbol_value)
     print(f"YOU WON {winnings} ")
     print(f"you won on these line", *winning_lines)
     return winnings-total

def main():
    balance=deposit()
    while True:
        print(f"CURRENT BALANCE IS${balance}")
        answer=input("PRESS ENTER TO PLAY & <q> to quit.")
        if answer =="q":
            break
        balance+=spin(balance)

    print(f"YOU ARE LEFT WITH ${balance}")

main()