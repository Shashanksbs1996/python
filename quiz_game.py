print("Welcome to my  Quiz Game ")

reply = input("Do you want to play a game with me ").lower()
if reply != "yes":
    quit()

print("Okay Let's Play the game ")
count =0

answer =input("who is the CEO of Facebook").lower()
if answer == "mark zb":
    count+=1
    print ("correct")

answer =input("who is the CEO of Tesla").lower()
if answer == "elon musk":
    count+=1
    print ("correct")

answer =input("who is the CEO of google").lower()
if answer == "satya nadela":
    count+=1
    print ("correct")

answer =input("Is the CEO of Twitter is indian").lower()
if answer == "yes":
    count+=1
    print ("correct")

answer =input("who is the richest person in india ").lower()
if answer == "mukesh ambani":
    count+=1
    print ("correct")

print ("You Scored"+ str(count)+ "out of 5 Question")
