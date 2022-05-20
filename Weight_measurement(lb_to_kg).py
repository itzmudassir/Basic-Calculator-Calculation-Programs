name = input("Please enter your name: ")
weight = input("Please enter your weight in pounds: ")
kilos = float(weight) / float(2.205)
print("Hi! " + name.capitalize() + " Your Weight in kilos is: " + str(kilos)[0:4] + " kg")
