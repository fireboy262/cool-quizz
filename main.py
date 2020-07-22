Heroes = {"AAA" : "Starlord",
"ACA" : "Drax",
"ABA" : "Black Panther",
"ABB" : "Spiderman",
"BAA" : "Winter Soldier",
"BAB" : "Rocket Raccoon",
"BBA" : "Captain America",
"BBB" : "Iron Man",
"CAA" : "Groot",
"CAB" : "Hulk",
"CBA" : "Spiderman",
"CBB" : "Mantis",
"DAA" : "Thanos",
"DAB" : "Thor",
"DBA" : "Hawkeye",
"DBB" : "Black Widow"}

name = input("hello what is you name? \n")
ans = input("hi " + name + " do you want to play? (y or n) \n")
if ans =="y":
	print("yay")

question1 = input("what is your favorite color (choose a, b, or c) \n blue \n yellow \n red \n")
question2 = input("what is your favorite browser (choose a, b, or c) \n internet explorer \n firefox \n chrome \n")
question3 = input("what is your favorite game (choose a, b, or c) \n minecraft \n roblox \n fortnite \n")


choice = question1 + question2 + question3
wait = input("do you want to know which hero you are (Y or N):")

if wait.upper() == "Y":
	print("you are " + Heroes[choice.upper()])
else:
	print("too bad")



