def welcome_user(game):
    import prompt
    from brain_even import val

    print('Welcome to the Brain Games! ')
    import prompt
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    game()
    answer = prompt.string('Your answer: ')
    if answer ==  val:
        print('Correct!')
        count += 1
    else:
        print(f"'{answer}'", 'is wrong answer ;(. Correct answer was ', f"'{val}'")
        print("Let's try again, " + name + '!')
        exit()
    if count == 3:
        print('Congratulations, ' + name + '!')