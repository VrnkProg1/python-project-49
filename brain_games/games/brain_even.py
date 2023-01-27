def even(x):
    from random import randint
    import prompt
    from brain_games.game_engine import name1 
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        a = randint(1, 100)
        if a % 2 == 0:
            value = 'yes'
        elif a % 2 != 0:
            value = 'no'
        print('Question: ', a)
        answer = prompt.string('Your answer: ')
        if answer == value:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}'", 'is wrong answer ;(. Correct answer was ', f"'{value}'")
            print("Let's try again, " + name1 + '!')
            break
        if count == 3:
            print('Congratulations, ' + name1 + '!')
