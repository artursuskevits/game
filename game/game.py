from random import *
#game
p=0
g=1
results=[]
bot_variant=["rock", "paper", "scissors"]
try:
    who = int(input("you want play vs bot(print 1) or friend(print 2)"))
    while who ==1 or who ==2   :
        if who == 1:
            you_variant=str(input("choose rock, paper or scissors"))
            i=choice(bot_variant)
            print(i)
            if you_variant == i:
                print("draw")
                a= ("you have draw vs bot")
                p+=1
                results.insert(p,a)
                print(results)
            elif you_variant == "rock" and i == "scissors":
                print("you win")
                a= ("you win vs bot")
                p+=1
                results.insert(p,a)
                print(results)
            elif you_variant == "scissors" and i == "paper":
                print("you win")
                a= ("you win vs bot")
                p+=1
                results.insert(p,a)
                print(results)
            elif you_variant == "paper" and i == "rock":
                print("you win")
                a= ("you win vs bot")
                p+=1
                results.insert(p,a)
                print(results)
            elif you_variant !=  "paper" and you_variant != "rock" and you_variant != "scissors":
                print("you cheater")
            else:
                print("bot win")
                a= ("bot win vs you")
                p+=1
                results.insert(p,a)
                print(results)

        elif who ==2:
            you_variant=str(input("you choose rock, paper or scissors"))
            you_variant2=str(input("friend choose rock, paper or scissors"))
            if you_variant == you_variant2:
                print("draw")
                a= ("you have draw vs friend")
                p+=1
                results.insert(p,a)
                print(results)
            elif you_variant == "rock" and you_variant2 == "scissors":
                print("you win")
                a= ("you win vs friend")
                p+=1
                results.insert(p,a)
                print(results)
            elif you_variant == "scissors" and you_variant2 == "paper":
                print("you win")
                a= ("you win vs friend")
                p+=1
                results.insert(p,a)
                print(results)
            elif you_variant == "paper" and you_variant2 == "rock":
                print("you win")
                a= ("you win vs friend")
                p+=1
                results.insert(p,a)
                print(results)
            elif you_variant !=  "paper" and you_variant != "rock" and you_variant != "scissors" or you_variant =="" :
                print("you cheater")
            elif you_variant2 !=  "paper" and you_variant2 != "rock" and you_variant2 != "scissors":
                print("friend cheater")
            else:
                print("friend win")
                a= ("friend win vs you")
                p+=1
                results.insert(p,a)
                print(results)
except:
    print("viga")
