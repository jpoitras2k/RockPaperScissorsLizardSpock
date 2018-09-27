''' DEVELOPER: JASON POITRAS
This is the classic rock, paper, scisors, lizard, spock from Big Bang Theory. 
RULES:
Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
(and as it always has) Rock crushes Scissors
'''

from random import randint

#computer guess from list
game_list = ['r', 'p', 's', 'l', 'sp']
cpu = game_list[randint(0,4)]
print("Play: Rock, Paper, Scissors, Lizard, Spock")

#player guess
player = input('Rock(r) ' 'Paper(p) ' 'Scissors(s) ' 'Lizard(l) ' 'or Spock(sp) ? ')
print ('The computer chose:',cpu)

if player == cpu:
    print('Its a Tie!')
elif player == 's' and cpu == 'p':
    print ('Scissors slices and dices paper, you win.')
elif player == 's' and cpu == 'l':
    print ('Scissors decapitates lizard, you win.')    
elif player == 'p' and cpu == 'r':
    print ('Paper covers rock, you won.')
elif player == 'p' and cpu == 'sp':
    print ('Paper disproves Spock, you won.')
elif player == 'r' and cpu == 'l':
    print ('Rock crushes lizard, you win')
elif player == 'r' and cpu == 's':
    print ('Rock smashes scissors, you win')
elif player == 'l' and cpu == 'sp':
    print ('You chose a strong lizard and poisoned Spock, you won.')
elif player == 'l' and cpu == 'p':
    print ('Your lizard ate all the paper, you won.')
elif player == 'sp' and cpu == 's':
    print ('Spock says live long and prosper after smashing scissors.  You won.')    
elif player == 'sp' and cpu == 'r':
    print ('Spock vaporized rock.  You won.')
else:
    print('The CPU won, too bad!')

