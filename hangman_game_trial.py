import time,random
with open('C:\\Users\\crockroax\\Desktop\\Projects\\Hangman_game using Python\\data _set for the word.txt','rt') as f:
    x=f.readlines()
word=random.choice(x)[:-1]
print('Welcome to the Hangman Game')
p=str(input("Enter Player name : "))
no_of_chances=random.randrange(1,10)
word_list=list(word)
temp=['_']*len(word_list)
print('You have got ',no_of_chances,' chances to guess the word with current status ',' '.join(temp))
while no_of_chances>0:
    print('....................................................................................')
    print('....................................................................................')
    x=str(input('Guess the letter with chances remaning '+str(no_of_chances)+': '))
    if x.lower() in word_list or x.upper() in word_list :
        for i in range(len(word_list)):
            if word_list[i]==x.upper() or word_list[i]==x.lower():
                temp[i]=word_list[i]
        print('current status: ',' '.join(temp))
    else:
        print('current status: ',' '.join(temp))
        no_of_chances-=1
        continue
    if ''.join(temp)==word:
        print('YOU WON!!',p,'The word was',word)
        break
else:
    print('YOU LOST THE GAME!!!',p,'The word was',word)




    
