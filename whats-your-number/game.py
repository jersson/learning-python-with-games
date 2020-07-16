begin = 0
end = 100
input_answer = ''

print('Please think of a number between {} and {}!'.format(begin, end))
guess = int((begin + end) / 2)

while input_answer != 'c':
    print('- Is your secret number {}?'.format(guess))
    print('Enter:')
    print("- 'h' to indicate the guess is too high. \n- 'l' to indicate the guess is too low. \n- 'c' to indicate I guessed correctly.")
    input_answer = input('Your answer...')
    if input_answer == 'l':
        begin = guess
        guess = int((begin + end) / 2)
    elif input_answer == 'h':
        end = guess
        guess = int((begin + end) / 2)
    elif input_answer != 'c':
        print('Sorry, I did not understand your input.')
print("- Game over.\n Your secret number is: {}".format(guess))
