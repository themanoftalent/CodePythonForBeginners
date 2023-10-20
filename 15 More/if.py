number = 51
guess = int(input('Enter an integer : '))

if guess == number:
    # New block starts here
    print('Congratulations, you guessed it.')
    
    
elif guess < number:
    # Another block
    print('No, it is a little higher than that')
    

else:
    print('No, it is a little lower than that')
  

print('Done')

