import random
import time

print "-" * 50
print "Welcome to a Game of Head or Tails."
print "Winners Survive, Losers DIE."
print "-" * 50
prompt = ">"

print "What's your name? "
name = raw_input(prompt)

print "How many games do you want to play?"
games = input()
user_count = 0
com_count = 0

for number in range (1, games+1):
    print "\nGame: %r \n" % number

    print "%s, Will it be Head or Tails?" % name
    choice = raw_input(prompt)
    print "You've chosen: %r\n" % choice

    
    if (choice == 'Head' or choice == 'Tails'):
        print "Tossing the Coin"
        time.sleep(1)
        print "*" * 50
        items = ['Head', 'Tails']
        answer = random.choice(items)
        if (answer == choice):
            user_count += 1
            print "It's %r. Congrats, you Won" % answer
        else:
            print "It's %r. Sorry, Computer won" % answer
            com_count += 1
        print "*" * 50
    else:
        print "-" * 50
        print "ERROR!!!! Please enter Head or Tails only"
        print "-" * 50

print "-" * 50
print "%r: %r   Computer: %r \n" % (name, user_count, com_count)
print "-" * 50
