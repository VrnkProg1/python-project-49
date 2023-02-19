import prompt


def hull_of_game(rulesarg, game):  # noqa: C901
    print('Welcome to the Brain Games! ')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    count = 0
    rules = rulesarg()
    print(rules)
    while count < 3:
        correct, question, expression = game()
        print(question, expression)
        #elif correct == int(correct):
            #expected_answer = str(correct)
        answer = prompt.string('Your answer: ')
        if correct == answer:
            expected_answer = correct
            print('Correct!')
            count += 1
        elif correct != answer:
            expected_answer = correct
            wrong = 'is wrong answer ;(. Correct answer was'
            print(f"'{answer}' {wrong} '{expected_answer}'")
            print("Let's try again, " + name + '!')
            return
        #elif correct == 'True' and answer == 'no':
            #wrong = 'is wrong answer ;(. Correct answer was'
            #print(f"'{answer}' {wrong} '{expected_answer}'")
            #print("Let's try again, " + name + '!')
            #return
        #elif int(answer) == correct:
            #print('Correct!')
            #count += 1
        #elif int(answer) != correct:
            #wrong = 'is wrong answer ;(. Correct answer was'
            #print(f"'{answer}' {wrong} '{expected_answer}'")
            #print("Let's try again, " + name + '!')
            #return
    print('Congratulations, ' + name + '!')
