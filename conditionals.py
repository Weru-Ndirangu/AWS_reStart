userReply= input("Do you need to ship a package? (Enter Yes or No) ")

if userReply =="yes":
    print("We can Help you ship that package!")
else: 
    print("Please come back when you need to ship a package. Thank You!")


userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from. You can explore them below...")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from. Explore them Below....")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number)")
    print("Here are {} copies.".format(copies))
else:
    print("Thank You! Please come again.")

