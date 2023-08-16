import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value={
    "A":2,
    "B":4,
    "C":4,
    "D":3
}

def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winnings+=values[symbol]*bet
            winning_lines.append(line+1)
    return winnings,winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol, symbol_count in symbols.items():#.items() gives both key and value assosciatede with the dictionary
        for _ in range(symbol_count): #_ anonymous variable used when we dont care about the count and helps save the memory
            all_symbols.append(symbol)
    columns=[]
    for col in range(cols):
        column=[]
        cur_symbols=all_symbols[:] #we add the slicing operator to create a copy so that the copy  doesnt reference the same object as old one as any modificationbs to either of em reflects on both
        for row in range(rows):
            value=random.choice(cur_symbols)# we are using a copy beacuse after slection we want to remove that varible so as to avoid the violation of the variable count in org dictionary
            cur_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end='')
        print()

def deposit():
    while True:
        amt=input("what would you like to deposit? $")
        if amt.isdigit():
            amt=int(amt)
            if amt>0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amt

def get_number_of_lines():
    while True:
        lines=input("Enter the number of lines to bet on (1-"+ str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amt=input("what would you like to bet on each line? $")
        if amt.isdigit():
            amt=int(amt)
            if MIN_BET<=amt<=MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amt

def spin(bal):
    lines=get_number_of_lines()
    while True:
        bet=get_bet()
        tot_bet=bet*lines
        if tot_bet>bal:
            print(f"You do not have enough balance to bet that amount, your current balance is ${bal}")
        else:
            break
    print(f"You are betting ${bet} on {lines}. Total bet is equal to: ${tot_bet}")
    slots=get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines=check_winnings(slots,lines,bet,symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines:",*winning_lines)
    return winnings-tot_bet

def main():
    bal=deposit()
    while True:
        print(f"Current balance is ${bal}")
        ans=input("Press enter to play (q to quit).")
        if ans=="q":
            break
        bal+=spin(bal)
    print(f"You are left with ${bal}")

main()