name = input("Enter a family member name:")
#name = name.capitalize
#print(name)

if name == "Raju":
    print(f"{name} is your Dad")
if name =="Subhashini":
    print(f"{name} is your Mum")
if name == "Jessica":
    print(f"{name} is your Sister")
if name =="Adarsh":
    print(f"{name} is you!")
if name != "Raju" or name != "Subhashini" or name != "Jessica" or name != "Adarsh":
    print(f"{name} is not a family member.")

