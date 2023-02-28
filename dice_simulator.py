''' wap to create a function that wil generate ramdom 
dice numbers and if all 3 match, then display 
"you win" else display "you lose / try again"'''
'''import random as rnd
def dice():
    l1=[1,2,3,4,5,6]
    l2=[1,2,3,4,5,6]
    l3=[1,2,3,4,5,6]
    
    r1=rnd.choices(l1)
    r2=rnd.choices(l2)
    r3=rnd.choices(l3)
    
    if(r1==r2 and r2==r3):
        print(f"{r1} {r2} {r3} you win🏆")
    else:
        print(f"{r1} {r2} {r3} better luck next time👎")
        
dice()'''

import random
def streak():
    dices=['1','2','3','4','5','6']
    selection=random.choices(dices, k=3)
    if selection[0]==selection[1]==selection[2]:
        return selection, "You Win🏆"
    else:
        return selection, "You lose👎"
    
ans,msg=streak()
print('rolling the dices...')
print(" ".join(ans))
print(msg)