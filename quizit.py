import random
import wakeup
from colors import termcolors



class crystatic:
    
    
    def glossary_quiz(file):
        # Initialize Variables
        score = 0
        counter = 0
        
        # Initialize Lists
        textfile = []
        questions = []
        
        # Takes everything from text file and adds each line to a list
        textfile = open(file).readlines()
        
        # Cleans up the textfile list by removing \n with the rstrip method
        for question in textfile:
            questions.append(question.rstrip())
            
        print("==================\n" +
            f'Welcome to my {termcolors.FAIL}Hell{termcolors.ENDC}\n' +
            "==================\n")
            
        # Initialize Keeper List for random counts called so we don't duplicate a question.
        keeper = []
            
        # Basically the method inside the method if we wanted to call a certain text file but this isnt for the public so I am keeping it this way
        for count in range(0, len(questions) - 1, 2):
            
            # Random count
            count = random.randrange(0, len(questions) - 1, 2)
            
            # Check if random count has already been called
            while questions[count] in keeper:
                # Code to view if duplicate is found. Shows that the while loop is working properly.
                # print(f'{termcolors.FAIL}Found duplicate{termcolors.ENDC}')
                count = random.randrange(0, len(questions) - 1, 2)
            
            # If random count has not already been chosen, append to keeper list.
            keeper.append(questions[count])
            
            # Code to view keeper list.
            # print(f'{keeper}\n')
            
            # Create a Multiple Choice List
            multiple_choice = []
            
            # Append the Correct Answer to the List
            multiple_choice.append(questions[count + 1])
            
            # Append 3 incorrect answers to the list
            multiple_choice.append(questions[random.randrange(1, len(questions) - 1, 2)])
            multiple_choice.append(questions[random.randrange(1, len(questions) - 1, 2)])
            multiple_choice.append(questions[random.randrange(1, len(questions) - 1, 2)])
            
            # Shuffle List
            random.shuffle(multiple_choice)
            
            print(f'A: {multiple_choice[0]}\n')
            print(f'B: {multiple_choice[1]}\n')
            print(f'C: {multiple_choice[2]}\n')
            print(f'D: {multiple_choice[3]}\n\n')
            
            # Take in Answer from User A-D.lower() of course
            answer = input(f'Define \'{questions[count]}\': ')
            
            # if answer is correct or incorrect logic
            if answer.lower() == 'a': 
                if questions[count + 1].lower() == multiple_choice[0].lower():
                    score += 1
                    print(f'\n=============\n\n{termcolors.OKGREEN}Correct{termcolors.ENDC}!')
                    print(f'Current Score: {score} out of {counter + 1}')
                    counter += 1
                else:
                    score += 0
                    print(f'\n=============\n\n{termcolors.WARNING}Wrong{termcolors.ENDC} answer but keep trying!')
                    print(f'Current Score: {score} out of {counter + 1}')
                    counter += 1
            elif answer.lower() == 'b': 
                if questions[count + 1].lower() == multiple_choice[1].lower():
                    score += 1
                    print(f'\n=============\n\n{termcolors.OKGREEN}Correct{termcolors.ENDC}!')
                    print(f'Current Score: {score} out of {counter + 1}')
                    counter += 1
                else:
                    score += 0
                    print(f'\n=============\n\n{termcolors.WARNING}Wrong{termcolors.ENDC} answer but keep trying!')
                    print(f'Current Score: {score} out of {counter + 1}')
                    counter += 1
            elif answer.lower() == 'c': 
                if questions[count + 1].lower() == multiple_choice[2].lower():
                    score += 1
                    print(f'\n=============\n\n{termcolors.OKGREEN}Correct{termcolors.ENDC}!')
                    print(f'Current Score: {score} out of {counter + 1}')
                    counter += 1
                else:
                    score += 0
                    print(f'\n=============\n\n{termcolors.WARNING}Wrong{termcolors.ENDC} answer but keep trying!')
                    print(f'Current Score: {score} out of {counter + 1}')
                    counter += 1
            elif answer.lower() == 'd': 
                if questions[count + 1].lower() == multiple_choice[3].lower():
                    score += 1
                    print(f'\n=============\n\n{termcolors.OKGREEN}Correct{termcolors.ENDC}!')
                    print(f'Current Score: {score} out of {counter + 1}')
                    counter += 1
                else:
                    score += 0
                    print(f'\n=============\n\n{termcolors.WARNING}Wrong{termcolors.ENDC} answer but keep trying!')
                    print(f'Current Score: {score} out of {counter + 1}')
                    counter += 1
            else:
                input('\nNext time, please choose a letter A-D .. Moving On Now .. btw -10 score for testing me')
                score += -10
                counter += 1
                antsy = input('\nAre you trying to return to the main menu? Type yes or no. If you are trying to exit the program hit ctrl + c or just type exit. \n\n')
                
                if antsy.lower() == 'yes':
                    wakeup.greetings.menu()
                elif antsy.lower() == 'no':
                    print('\nSkipping Question...\n\n')
                    continue
                else:
                    exit()
            
            # Aesthetics
            try:
                current_percentage = int(score / counter * 100)
                
                if current_percentage > 89:
                    current_percentage = f'{termcolors.OKGREEN}{current_percentage}{termcolors.ENDC}'
                elif current_percentage < 90 and current_percentage > 59:
                    current_percentage = f'{termcolors.OKCYAN}{current_percentage}{termcolors.ENDC}'
                elif current_percentage < 70 and current_percentage > 39:
                    current_percentage = f'{termcolors.WARNING}{current_percentage}{termcolors.ENDC}'
                else:
                    current_percentage = f'{termcolors.FAIL}{current_percentage}{termcolors.ENDC}'
                
                print(f'Currect Percentage: {current_percentage}%')
            
            except ZeroDivisionError:
                print('Not today sonny')
            
            print(f'Remaining questions: {int(len(questions) / 2 - counter)}\n\n=============\n')
            
            # Clear list to start afresh
            multiple_choice.clear()
            
        input('You actually did all those questions? You bored bastard. Press enter to go touch grass.')
        goagain = input('\n1. Go Touch Grass (gtg)\n2. Back to Main Menu\n\n')
        
        if goagain == '2':
                    wakeup.greetings.menu()             
        else:
            exit()