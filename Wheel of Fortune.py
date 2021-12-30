#!/usr/bin/env python
# coding: utf-8

# # Wheel of Fortune Game
# ### Connor Buxton, 12/26/21
# This is a game for three players which follows loosely the rules from the titular gameshow.

# In[62]:


import random


# In[63]:


def introDisplay():
    introString = '''
    Welcome to the fabulous
    ************************
    *** WHEEL OF FORTUNE ***
    ************************
    ----------------------------------------------------------------------------------------------------
    HOW TO PLAY:
    This game has 3 players who take turns spinning a wheel which has 24 slices.
    The slices can be monetary values ranging from $100 - $900, or titled
    LOSE A TURN or BANKRUPT. Both cause you to lose your turn, but the
    BANKRUPT slice also makes you lose any money you've accrued.
    
    The objective of the game is to earn money by guessing letters out of the selected word.
    When a player lands on a money slice, they have the opportunity to earn that much money
    by correctly guessing a consonant that appears in the blanked out word. If they succeed,
    they can also buy a vowel for $250. After that, they can try to guess the word and by doing
    so, they are able to keep all the money they've accrued for the next rounds. The other players
    are reset to $0.
    
    STANDARD ROUND:
    The rules above apply for the two standard rounds. The player who guesses the word retains the money
    they've earned, while the other two players are reset back to $0. The player who has the highest
    total earned moves onto the final round.
    
    FINAL ROUND:
    In the final round, there is only one player and the rules are quite different. A word is picked and
    the letters R, S, T, L, N and E are revealed for free. The player still standing at this stage can
    guess 3 consonants and 1 vowel. Once this is all done, the player must guess the word to earn the
    money they accrued over the previous two rounds. If they get it wrong, they get nothing.
    ----------------------------------------------------------------------------------------------------
    '''
    
    print(introString)


# In[64]:


def getPlayerNames(player_dict, player_slot):
    # Function purpose: intermediate function for use in getPlayers, lets them input their name
    goodInput = False
    count = 0
    
    while not goodInput:
        tempName = input(f'Enter Player {player_slot}\'s name: ')
        splitName = tempName.split()
        for item in splitName:
            if item.isalpha():
                count += 1
                
        if count == len(splitName):
            player_dict['name'] = tempName
            goodInput = True
            
        else:
            print('That is not a name. Try again.')
            


# In[65]:


def selectWord():
    # Function purpose: selects a word for guessing, returns it and a blanked version of it in the form of a list
    x = 0
    rand_num = random.randint(0, 370102)
    f = open('words_alpha.txt', 'r')
    while x <= rand_num:
        sample_line = f.readline()
        x += 1
    f.close()

            
    picked_word = sample_line.strip()
    picked_word = picked_word.lower()
    
    mystery_word = '_ '*len(picked_word)
    mystery_word = mystery_word.strip()
    mystery_list = mystery_word.split()
    
    return picked_word, mystery_list


# In[66]:


def checkGuess(user_guess, picked_word, mystery_list, guess_type):
    # Function purpose: check a player's guess, replace blanks with replaceBlanks, and let the round function know
    # if they got it
    if guess_type == 'letter':
        if user_guess.lower() in picked_word:
            print('You got a letter right!')
            mystery_list = replaceBlanks(user_guess, picked_word, mystery_list)
            correct_guess = True
        else:
            print('Sorry, that letter isn\'t in the word.')
            correct_guess = False
            
    if guess_type == 'word':
        if user_guess.lower() == picked_word:
            print('You got the word right!')
            picked_list = []
            for i in range(len(picked_word)):
                picked_list.append(picked_word[i])
            mystery_list = picked_list
            correct_guess = True
        else:
            print('Sorry, that isn\'t the word.')
            correct_guess = False
            
    return correct_guess, mystery_list


# In[67]:


def finalReveal(letter, picked_word, mystery_list):
    # Function purpose: same as checkGuess, but no printing - final round only
    mystery_list = replaceBlanks(letter, picked_word, mystery_list)
    
    return mystery_list


# In[68]:


def replaceBlanks(user_guess, picked_word, mystery_list):
    # Function purpose: reveal letters in blanked out version of picked word
    letter_in_word = True
    starting_position = 0
    while letter_in_word:
        letter_index = picked_word.find(user_guess, starting_position)
        if letter_index > -1:
            mystery_list[letter_index] = user_guess.lower()
            starting_position = letter_index + 1
        
        else:
            letter_in_word = False
            
    return mystery_list


# In[69]:


def spinWheel():
    # Function purpose: spin that wheel, tell the rest of the code what it got
    spin = random.randint(0, 23)
    spinList = (100, 100, 150, 200, 200, 250, 300, 300, 350, 400, 400, 450, 500, 500, 550, 600, 650, 700, 750, 800, 850, 900, 0, -1)
    wheel_slice = spinList[spin]
        
    return wheel_slice


# In[70]:


def getPlayers():
    # Function purpose: get player dictionaries set up and get names
    player_one = {'name': None, 'money': 0, 'bank': 0}
    getPlayerNames(player_one, 1)
    player_two = {'name': None, 'money': 0, 'bank': 0}
    getPlayerNames(player_two, 2)
    player_three = {'name': None, 'money': 0, 'bank': 0}
    getPlayerNames(player_three, 3)
    
    multiplayer = (player_one, player_two, player_three)
    return multiplayer


# In[80]:


def standardRound(multiplayer):
    print()
    print()
    # win_status to break loop when game won
    win_status = False
    # lists to store guessed consonants and vowels
    stored_consonants = []
    stored_vowels = []
    # list for vowels
    vowels = ('a','e','i','o','u')
    # if all the vowels are guessed, no one should be able to buy one
    all_vowels_guessed = False
    # select word and blank it out
    picked_word, mystery_list = selectWord()
    # word check to see if they guessed it correctly
    word_correct = False
    # debug for printing word for testing
    print('Debug: ' + picked_word)
    
    # round loop
    while not win_status:
        # for each player...
        for x in range(3):
            # print their stuff
            print(f'Player {x+1}\'s Turn!')
            print(str(multiplayer[x]['name']) + ': $' + str(multiplayer[x]['money']))
            print('The word is ' + str(''.join(mystery_list)))
            print('Spinning the wheel...')
            print()
            # spin that wheel
            spin_result = spinWheel()
            # if spin is money
            if spin_result >= 100 and spin_result <= 900:
                print(f'The wheel landed on ${spin_result}.')
                good_input = False
                # check input before accepting, is it consonant, vowel, word, etc...
                while not good_input:
                    player_guess = input('Please enter a consonant, or try to guess the word: ')
                    player_guess = player_guess.lower()
                    if player_guess.isalpha() and player_guess not in vowels and player_guess not in stored_consonants and len(player_guess) == 1:
                        # good guess
                        correct_guess, mystery_list = checkGuess(player_guess, picked_word, mystery_list, 'letter')
                        if correct_guess:
                            # guess is right, give them their money
                            multiplayer[x]['money'] += spin_result
                            # print the word with the new revealed letters
                            print('The word is ' + str(''.join(mystery_list)))
                            if multiplayer[x]['money'] >= 250:
                                # if their money is greater or equal to $250, ask if they want to buy a vowel
                                secondary_input = False
                                while not secondary_input and stored_vowels != vowels:
                                    vowel_ask = input('Would you like to buy a vowel? [y/n]: ')
                                    if vowel_ask.lower() == 'y':
                                        # buying a vowel
                                        vowel_input = False
                                        while not vowel_input:
                                            vowel_guess = input('Please input a vowel [a, e, i, o, u]: ')
                                            if vowel_guess in vowels and vowel_guess not in stored_vowels:
                                                discard, mystery_list = checkGuess(vowel_guess, picked_word, mystery_list, 'letter')
                                                if discard:
                                                    # they got a letter right, show updated word
                                                    print('The word is ' + str(''.join(mystery_list)))
                                                stored_vowels.append(vowel_guess)
                                                vowel_input = True
                                                
                                            elif vowel_guess in stored_vowels:
                                                print('Sorry, that vowel has already been picked.')
                                            else:
                                                print('That is not a vowel, please try again.')
                                        # subtract their money after all that
                                        multiplayer[x]['money'] -= 250
                                        secondary_input = True
                                    elif vowel_ask.lower() == 'n':
                                        # don't want a vowel
                                        secondary_input = True
                                    else:
                                        # IDK
                                        print('Sorry, please input a Y or an N.')
                                
                            word_input = False
                            while not word_input:
                                # ask if they want to try and guess the word
                                word_ask = input('Would you like to try and guess the word? [y/n]: ')
                                if word_ask.lower() == 'y':
                                    word_guess = input('Input a word: ')
                                    temp, mystery_list = checkGuess(word_guess, picked_word, mystery_list, 'word')
                                    if temp:
                                        word_correct = True
                                    word_input = True
                                elif word_ask.lower() == 'n':
                                    word_input = True
                                    
                        stored_consonants.append(player_guess)
                        # store a consonant guess to prevent from same guesses for money
                        mystery_check = ''.join(mystery_list)
                        # check whether word is all revealed
                        if mystery_check == picked_word:
                            word_correct = True
                        good_input = True
                        
                    elif player_guess.isalpha() and len(player_guess) > 1:
                        # word guess - same as just above, but at the beginning of the turn. Placed here so that game doesn't get stuck
                        temp, mystery_list = checkGuess(player_guess, picked_word, mystery_list, 'word')
                        if temp:
                            # correct guess, they got the word
                            word_correct = True
                        good_input = True
                                
                    elif player_guess in stored_consonants:
                        # don't let player guess the same thing
                        print('Sorry, that consonant has already been picked.')
                        
                    elif player_guess in vowels:
                        # no vowel guess allowed at consonant stage
                        print('That is a vowel, not a consonant. Try again.')
                        
                    else:
                        # IDK - computer saying that, this is just a catchall
                        print('I couldn\'t recognize your input. Try again.')
                        
            elif spin_result == 0:
                print('The wheel landed on Lose a Turn!')
                # no action - goes to next player turn
                
            else:
                print('The wheel landed on BANKRUPT!!!')
                multiplayer[x]['money'] = 0
                # sets player X's money to 0 and goes to next player turn
            
            
            print()
            print()
            if word_correct:
                break
                # if the word is guessed or all revealed, stop for loop and don't go to next player
                
        mystery_join = ''.join(mystery_list)
        if mystery_join == picked_word:
            # The word has been guessed
            win_status = True
            
    # big section - set up banks if player has most money
    
    # add up each player's money and bank:
    player_one_total = multiplayer[0]['money'] + multiplayer[0]['bank']
    player_two_total = multiplayer[1]['money'] + multiplayer[1]['bank']
    player_three_total = multiplayer[2]['money'] + multiplayer[2]['bank']
    if player_one_total >= player_two_total and player_one_total >= player_three_total:
        multiplayer[0]['bank'] = multiplayer[0]['money']
        winner_bank = multiplayer[0]['bank']
        print(f'Player 1 has won this round with ${winner_bank}!')
    elif player_two_total >= player_one_total and player_two_total >= player_three_total:
        multiplayer[1]['bank'] = multiplayer[1]['money']
        winner_bank = multiplayer[1]['bank']
        print(f'Player 2 has won this round with ${winner_bank}!')
    else:
        multiplayer[2]['bank'] = multiplayer[2]['money']
        winner_bank = multiplayer[2]['bank']
        print(f'Player 3 has won this round with ${winner_bank}!')
            
    # reset money for next round - keep banks though
    multiplayer[0]['money'] = 0
    multiplayer[1]['money'] = 0
    multiplayer[2]['money'] = 0
    
    # return the multiplayer dictionary for use in next round or final round
    return multiplayer


# In[81]:


def finalRound(player_dict):
    # get their name and bank amount
    player_name = player_dict['name']
    player_bank = player_dict['bank']
    stored_consonants = []
    # print friendly messages
    print(f'Welcome, {player_name}, to the final round!')
    print(f'You\'ve got ${player_bank} riding on the line, in addition to a $1000 dollar bonus prize!')
    # pick word and blanked out version
    picked_word, mystery_list = selectWord()
    print('Let\'s see the word...')
    print('Debug: ' + picked_word)
    # reveal letters as below
    reveal_list = ('r', 's', 't', 'l', 'n', 'e')
    # use for checking vowel input
    vowels = ('a', 'e', 'i', 'o', 'u')
    
    # reveal all in reveal_list
    for item in reveal_list:
        mystery_list = finalReveal(item, picked_word, mystery_list)
    print(str(' '.join(mystery_list)))
    # add those guys to the stored_consonants to prevent guessing them later on
    stored_consonants.extend(reveal_list)
    
    print('Pick three consonants other than R, S, T, L, N and E.')
    # three guesses, consonants only
    for x in range(3):
        good_input = False
        while not good_input:
            finalist_guess = input('Enter a consonant: ')
            finalist_guess = finalist_guess.lower()
            if finalist_guess.isalpha() and finalist_guess not in vowels and finalist_guess not in stored_consonants and len(finalist_guess) == 1:
                temp, mystery_list = checkGuess(finalist_guess, picked_word, mystery_list, 'letter')
                good_input = True
            else:
                print('That is not a consonant. Try again.')
                
        print('The word is: ' + ' '.join(mystery_list))
        print()
            
            
    print('Pick a vowel.')
    # one vowel guess
    vowel_input = False
    while not vowel_input:
        finalist_vowel_guess = input('Enter a vowel other than E: ')
        finalist_vowel_guess = finalist_vowel_guess.lower()
        if finalist_vowel_guess in vowels and finalist_vowel_guess != 'e':
            temp, mystery_list = checkGuess(finalist_vowel_guess, picked_word, mystery_list, 'letter')
            vowel_input = True
        else:
            print('That is not a vowel. Try again.')
    
    # only one guess, one chance!
    print('You have one chance to guess the word and bring back all the money. Good luck.')
    print('The word is: ' + ' '.join(mystery_list))
    finalist_word = input('Enter a word: ')
    
    # either they got it or they don't
    if finalist_word.lower() == picked_word:
        print('Congratulations, you got it right!')
        print(f'{player_name}, you\'re bringing back ${player_bank + 1000} home!')
        
    else:
        print('Sorry, that isn\'t the word.')
        print(f'{player_name}, it was a pleasure to have you on the show.')


# Below is the main body for the game:

# In[82]:


# The actual game
introDisplay()

# get the player info set up
multiplayer = getPlayers()

# First round:
multiplayer = standardRound(multiplayer)

# Second round:
multiplayer = standardRound(multiplayer)

# Decide which player moves forward:
bankCheck = multiplayer[0]['bank']
slot = 0
if multiplayer[1]['bank'] >= bankCheck:
    slot = 1
    bankCheck = multiplayer[1]['bank']
if multiplayer[2]['bank'] >= bankCheck:
    slot = 2
    
# Final round:
finalRound(multiplayer[slot])
    
# End of game
print()
print('It was a pleasure to have everyone here! See you again soon!')


# In[ ]:





# In[ ]:




