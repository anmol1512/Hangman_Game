print('Welcome to the world of Hangman')
p1=str(input("Enter Player name 1: "))
p2=str(input("Enter Player name 2: "))
guesser=str(input("Enter the player who will guess: "))
no_of_chances=None
if guesser in list((p1,p2)):
    no_of_chances=int(input('Enter the no of chances given to the guesser:'))
else:
    print('Sorry!! you entered a wrong name kindly enter correct guesser')
    guesser=str(input("Enter again the player who will guess: "))
word=str(input('Enter the word which needs to be guessed'))
l=list(word)
temp=['_']*len(l)
while no_of_chances>0:
    print('....................................................................................')
    print('....................................................................................')
    x=str(input('Guess the word with chances remaning '+str(no_of_chances)+': '))
    if x in l:
        for i in range(len(l)):
            if l[i]==x:
                temp[i]=x
        print('original word: '+word)
        print('current status: '+str(''.join(temp)))
    else:
        print('original word: '+word)
        print('current status: '+str(''.join(temp)))
        no_of_chances-=1
        continue
    if ''.join(temp)==word:
        print('hence matched')
        break
else:
    print('LOST THE GAME!!!')




    
