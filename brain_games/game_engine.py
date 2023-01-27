def welcome_user(game):
    from brain_games.games.brain_even import value
    import prompt
    
    print('Welcome to the Brain Games! ')
    import prompt
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    game()
    answer = prompt.string('Your answer: ')
    if answer == value:
        print('Correct!')
        count += 1
    else:
        print(f"'{answer}'", 'is wrong answer ;(. Correct answer was ', f"'{value}'")
        print("Let's try again, " + name + '!')
        exit()
    if count == 3:
        print('Congratulations, ' + name + '!')
