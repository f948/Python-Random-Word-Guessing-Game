"""
Programmer:Eric
Date:12/7/2018
Purpose:To simulate a random word guessing game where the computer generates a
random scrambled word and the user tries to guess what it is

"""
import random

# global constant
LIST_OF_LISTS=[["toothbrush","lightsabre","suitofarmor","PythonBook","toilet","physics","machine"],
                               ["bedrock","looking","dominant","elastic","war"],
                               ["list","others","people","lighthouse"],
                               ["world","motherboard","option","essay"],
                               ["America","UnitedStates","homeless"],
                               ["celebrity","hammer","teeth","washingmachine","order"],
                               ["python","tuple","hanging","open","breakfast","island"],
                               ["internet","chose","insomanic","deravitive","beach"],
                               ["gothic","port","religious","top","hiking","operation"]]



            
def word_jumble(word):
    '''This function jumbles up the characters in a word by accepting a string
        as an arguement and returns a new string with all the characters but in
        a random order'''
    
    index_list=[]
    for index in range(len(word)):
        index_list+=[index]
    
    empty_list=[]
    for index in range(len(word)):
        empty_list+=[" "]
  
    new_word=""
    for character in word:
        new_word+=character+" "
    
    split_word=new_word.strip().split(" ")
   
    for character in split_word:
        index_value=random.choice(index_list)
        index_list.remove(index_value)
        empty_list[index_value]=character
        
    random_word=""
    for character in empty_list:
        random_word+=character
        
    return random_word

def check_user_answer(user_answer,word):
    '''This boolean function will check if the user's answer matches the original
        word by accepting the user's answer and unscrambled word as arguements
        and will return True if the answer is correct and False if it is
        incorrect'''
    
    if user_answer.strip()==word:
        return True
    else:
        return False
    
def display_main_menu():
    '''This function will display the main options menu for this program'''
    print("\n")
    print("RANDOM WORD GUESSING GAME")
    print("\n")
    print("Select:")
    print("1 to start")
    print("2 for help menu")
    print("\n")
    
def display_help_menu():
    '''This function will display the instructions on how to play the game
        for anyone who doesn't know'''
    print("\n")
    print("HELP")
    print("\n")
    print("This is a random guessing word game")
    print("1. The computer will choose a list of words")
    print("2.One word will be selected and scrambled")
    print("3.You will have to try to guess the unscrambled word")
    print("4.You win the game if you guess all the words in the list")
    print("\n")
    
# infinite loop keeps program running 
while True:
    display_main_menu()
    option=str(input("Choose an option"))

    # case when user chooses to play 
    if option=="1":
    
        word_bank = False
        play_again=True
        
        # main game loop
        while play_again:
            
            list_words=random.choice(LIST_OF_LISTS)

            choice=str(input("Do you want to see the word bank? Enter Y or y for yes and N or n for no(default value is no)"))

             # display word bank
            if choice =="Y" or choice == "y":
                word_bank= True
            
            # loop runs for one round
            while True:
    
                if len(list_words)>0:
                    word=random.choice(list_words)
                else:
                    break
                
                # case when user chooses to see a word bank 
                if word_bank:
                    print(list_words)
                    
                print("The scrambled word is:",word_jumble(word))
                user_answer=str(input("What do you think the word is?"))

                # break when user gets word correct 
                while not check_user_answer(user_answer,word):
                    print("Sorry, incorrect")
                    user_answer=str(input("What do you think the word is?"))

                print("Correct")
                list_words.remove(word)
                
            print("Congraulations you guessed all the words")
           
            choice=str(input("Would you like to play again? Y for yes n for no(default value is no)"))

            # exit game 
            if choice =="N" or choice == "n":
                play_again=False
                
        play_again = True
        word_bank = False

    # case when user chooses to look at instructions    
    elif option=="2":
        display_help_menu()
        
        
   

        
        
