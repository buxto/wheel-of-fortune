# wheel-of-fortune
TITLE:
    Connor Buxton's Wheel of Fortune Programming Project
    Date Completed 12/29/21

----------------------------------------------------
DESCRIPTION: 
    This project emulates the Wheel of Fortune
    game seen on TV. It is not a perfect copy, but quite
    similar. Overall, it performs well, but isn't very clean
    looking. Hopefully that will get better with more practice.

HOW TO RUN:
----------------------------------------------------------
    Run the py file in command line.

HOW TO PLAY:
----------------------------------------------------------
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
    
CREDITS:
Dev10 Team
