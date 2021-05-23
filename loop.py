#print("1")
#print("2")
#print("3")
#print("4")
#range(10)
print("Enter your timestable:")
tt = int(input()) # ----------------------------------------------------
print("Please enter the start number of your timestable:") #            |
s = int(input()) #------------------------------------------------------                                                    
print("Now please enter your end number:") #                            |
e = int(input()) #                                                      |
for i in range(s,e + 1): # no need to add 'int' because it is defined here.
 print(f'{tt} x {i} = {tt * i}')

