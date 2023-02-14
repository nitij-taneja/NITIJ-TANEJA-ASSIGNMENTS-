#stone paper scissor
#s=stone, p=paper, k=scissor
import random
import pyttsx3 as p
print("""
_______________________________________________________________
            Welcome To Stone Paper Scissor Game
_______________________________________________________________
""")
welcome=p.init()
welcome.say(" Welcome To Stone Paper Scissor Game")
welcome.runAndWait()

print("""Winning rules of the game Stone Paper Scissors are:

>>>Stone vs Paper -> Paper wins
>>>Stone vs Scissors -> Stone wins
>>>Paper vs Scissors -> Scissor wins

>>>s=stone, p=paper, k=scissor

Stone Paper Scissors!!!
""")
rules=p.init()
rules.say("""Winning rules of the game Stone Paper Scissors are
if Stone versus Paper then Paper wins
if Stone versus Scissors then Stone wins
if Paper versus Scissors then Scissor wins
YOU WILL BE GIVEN 5 CHANCES
SO LETS PLAY
STONE PAPER SCISSOR""")
rules.runAndWait()
lst=['s','p','k']
i=0
cs=0
us=0
while i<5:
    chances=5
    chances=chances-i
    mn=('Your chances left:',chances)
    print(mn)
    st=p.init()
    st.say(mn)
    st.runAndWait()
    print()
    j=random.randint(0,2)
    a=lst[j]
    m=p.init()
    m.say("choose between s p k")
    m.runAndWait()
    b=input('choose between s/p/k')
    z=('Computer Choice is',a)
    print(z)
    n=p.init()
    n.say(z)
    n.runAndWait()
    i+=1

    if a==b:
        print('no win and no loss')
        print()
        o=p.init()
        o.say("no win and loss")
        o.runAndWait()
        print('Scoreboard:')
        print('Computer Score:',cs, 'User Score:',us)
        print()

    elif (a=='s' and b=='p') or (a=='p' and b=='k') or (a=='k' and b=='s'):
        print('you won, congratulations')
        us+=1
        print()
        q=p.init()
        q.say("you won congratulations")
        q.runAndWait()
        print('Scoreboard:')
        print('Computer Score:',cs, 'User Score:',us)
        print()

    elif (a=='s' and b=='k') or (a=='p' and b=='s') or (a=='k' and b=='p'):
        print('computer won, hard luck')
        cs+=1
        print()
        s=p.init()
        s.say("computer won hard luck")
        s.runAndWait()
        print('Scoreboard:')
        print('Computer Score:',cs, 'User Score:',us)
        print()

print("THANKS FOR PLAYING")   
msg=p.init()
msg.say("thanks for playing")  
msg.runAndWait()


