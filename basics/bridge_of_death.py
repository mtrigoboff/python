import random as r

print('Monty Python and the Holy Grail - The Bridge of Death')
print('https://www.youtube.com/watch?v=0D7hFHfLEyk')
print()				    # print a blank line

print('Who would cross the Bridge of Death')
print('must answer me these questions three,')
print('ere the other side he see!')
print()			        # print a blank line

# read name from the user
name =	input('What is your name? ')

# read quest from the user
quest =	input('What is your quest? ')

# choices
rand_num = r.random()	# returns a random float between 0 and 1
if rand_num < .33:
    # read color from the user
    answer3 = input('What is your favorite color? ')
    print('\nRight! Off you go!')
elif rand_num >= .33 and rand_num < .67:
    # read capital from the user+
    answer3 = input('What is the capital of Assyria? ')
    if answer3.lower() == 'assur':
        print('\nRight! Off you go!')
    else:
        print('\nAaargh!')
else:
    # read airspeed from the user
    answer3 = input('What is the airspeed velocity of an unladen swallow? ')
    if answer3.lower() == 'african or european?':
        print('\n<bridge guardian is cast into the gorge>')
    else:
        print('\nAaargh!')
print()			        # print a blank line
