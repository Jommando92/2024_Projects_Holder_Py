import random

MAX_LINES = 3 # This is the maximum number of lines that can be read from the file.
MAX_BET = 100 # This is the maximum amount of money that can be bet.
MIN_BET = 1 # This is the minimum amount of money that can be bet.

ROWS = 3
COLS = 3

symbol_count = {
     "A":2,
     "B":4,
     "C":6,
     "D":8
}

symbol_value = {
     "A":5,
     "B":4,
     "C":3,
     "D":2
}

def check_winnings(columns, lines, bet, values):
     winning = 0
     winning_lines = []
     for line in range(lines):
          symbol = columns[0][line]
          for column in columns:
               symbol_to_check = column[line]
               if symbol != symbol_to_check:
                    break
          else:
               winning += values[symbol] * bet
               winning_lines.append(line + 1)

     return winning, winning_lines

def get_slot_machine_spin(rows, cols, symbols): # This function will be used to generate the slot machine spin.
     all_symbols = []
     for symbol, symbol_count in symbols.items(): # This will loop through the symbols.
          for _ in range(symbol_count): # This will loop through the symbol count.
               all_symbols.append(symbol)

     columns = []
     for _ in range(cols): # This will loop through the columns.
          column = []
          current_symbols = all_symbols[:] # This will copy the list of all symbols.
          for _ in range(rows):
               value = random.choice(current_symbols) # This will choose a random symbol from the list of all symbols.
               current_symbols.remove(value) # This will remove the symbol from the list of all symbols.
               column.append(value)

          columns.append(column)

     return columns

def print_slot_machine(columns): # This function will be used to print the slot machine.
     for row in range(len(columns[0])):
          for i,  column in enumerate(columns):
               if i != len(columns) - 1:
                    print(column[row],end =" | ")
               else:
                    print(column[row],end ="")

          print() # This will print a new line.


def deposit():  # This function will be used to deposit money into the account.
     while True:  # This will loop the code until the user inputs a valid amount.
          amount = input("Enter the amount you want to deposit:£")
          if amount.isdigit(): # This will check if the input is a digit.
               amount = int(amount) # This will convert the input into an integer.
               if amount > 0:
                    break
          else:
               print("Please enter a valid amount. Great than £0")
     else:
          print("Enter a Valid Number.")

     return amount

def get_number_of_lines():
     while True:
          lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
          if lines.isdigit():
               lines = int(lines)
               if 1 <= lines<= MAX_LINES:
                    break
               else:
                    print("Please enter a valid a valid of lines")
          else:
               print("Enter a Valid Number.")

     return lines


def get_bet():
     while True:
          amount = input("Enter the amount you want to bet on each line:£")
          if amount.isdigit():
               amount = int(amount)
               if MIN_BET <= amount <= MAX_BET:
                    break
               else:
                    print(f"Amount must be between £{MIN_BET} and £{MAX_BET}.")
               # This will print the minimum and maximum amount that can be bet.
          else:
               print("Enter a Valid Number.")
     return amount

def spin(balance):
     lines = get_number_of_lines()
     while True:
          bet = get_bet()
          total_bet = bet * lines

          if total_bet > balance:
               print(f"You do not have enough to bet that amount, your current balance is: £{balance}")
          else:
               break
          print(f"You are betting £{bet} on {lines} lines. Total bet is equal to: £{total_bet}")

     slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
     print_slot_machine(slots)
     winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
     print(f"You won £{winnings}.")
     print(f"You won on lines:", *winning_lines)
     return winnings - total_bet


def main():
     balance = deposit()
     while True:
          print(f"Current balance is ${balance}")
          answer = input("Press enter to play (q to quit).")
          if answer == "q":
               break
          balance += spin(balance)

     print(f"You left with £{balance}")

main()

#try out