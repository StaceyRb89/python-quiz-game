print("Welcome to my Quiz Game!")
"""
an equals is called an assignment 
"""
""" is the same as line 6"""
playing = input("Do you want to play? ")

"""Ah yeah, a single = is also the same as in JS where it assigns a value to a variable, but in Python there is no keyword to set a variable (let, var, const) so you just type the variable name, then =, then the value, for example:
num = 10
print(num)
In JS this would be something like:
let num = 10;
console.log(num);"""
if playing != "yes":
    quit()

print("Okay lets play! :)")
score = 0

answer = input("What does Hügelkultur stand for in permaculture? ")
if answer.lower() == "raised garden bed":
    print("Correct!")
    score = score + 1
elif answer.lower() == "quit":
    print("You chose to quit!")
    quit()
else:
    print("Incorrect!")

answer = input("In permaculture, what does NFT typically refer to? ")
if answer.lower() == "nutrient film technique":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

answer = input("What does SWC represent in permaculture design? ")
if answer.lower() == "sustainable water collection":
    print("Correct!") 
    score = score + 1  
else:
    print("Incorrect!") 

answer = input("What does TSP usually indicate in permaculture gardening? ")
if answer.lower() == "triple superphosphate":
    print("Correct!") 
    score = score + 1
else:
    print("Incorrect!")

print ("you got " + str(score) + "questions correct!")
print ("you got " + str((score / 4) * 100) + "%")