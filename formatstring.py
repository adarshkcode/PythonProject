name = input("Please enter your name:")
age = input("Please enter your age:")
txt = "Your name is {1}, and you are {0} years old."
print(txt.format(name,age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
