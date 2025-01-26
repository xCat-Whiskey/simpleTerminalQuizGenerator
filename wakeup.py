from quizit import crystatic

class greetings:
        
    def menu():
        print('\n\n1. Sample')

        try:
            userInput = int(input('\nEnter a number of your choosing.. just kidding, pick one on the screen.\n\n'))

            while userInput < 1 or userInput > 1:
                userInput = int(input('Please enter a number between 1 and ..uhm 1'))
                
        except ValueError:
            print()
            greetings.menu()

        match userInput:
            
            case 1:
                crystatic.glossary_quiz('textfiles/sample.txt')
            case _:
                input('Study Hard!')
                exit()