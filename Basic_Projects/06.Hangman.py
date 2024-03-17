import random

wordlist=["federation","tablet","prove","neighbourhood","eyeshadow"]
word=random.choice(wordlist)
for blank in range(0,len(word)):
    print("_",end="")
i=0  

eog=False  
while not eog:
    for i in range(0,len(word)): 
        print("Guess a letter")
        guess=input()
        guess=guess.lower()
        if guess in word:
    
            for i in range(0,len(word)):
           
                if word[i]==guess:

                    print(guess,end="")
                else:
                    print("_",end="")
            if "_" not in word:
                eog=True
                print("Won")
        else:
            print("No")