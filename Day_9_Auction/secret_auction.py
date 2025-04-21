from art import logo
from IPython.display import clear_output

print(logo)

print('Welcome to the secret auction program.')

bidder_details = {}

while True:
    name = input('\nWhat is your name? ')
    bid = float(input('\nWhat is your bid? $'))

    bidder_details[name] = bid

    someone_else = input('\nAre there any other bidders? Type "yes" or "no".').lower()

    while someone_else != 'yes' and someone_else != 'no':
        print('\nError. Please type "yes" or "no" to continue.')
        someone_else = input('\nAre there any other bidders? Type "yes" or "no".').lower()

    if someone_else == 'no':
        break
    elif someone_else == 'yes':
        clear_output(wait = True)

winning_bid = 0
winner = ''

for bidder in bidder_details:
    bid = bidder_details[bidder]
    if bid > winning_bid:
        winner = bidder
        winning_bid = bid

print(f'\nThe winner is {winner} with a bid of ${winning_bid}')



