#Please dont use this random passwords. The responsibility completely belong to you.


#--------------------------- Starting---------------------------------------# 
import random
randPasswordList= []
print("Random Password Generator")
print("-"*50)
 #--------------------------Sources------------------------------------------# 
numbers= [0,1,2,3,4,5,6,7,8,9]
letters= ["A","B", "C", "D" , "E", "F", "G" ,"H",  "İ" , "J",  "K", "L" ,  "M", "N" , "O" , "P"  ,"R", "S", "T", "U", "V", "W", "X", "Y",  "Z"   ]
sLetters= ["a", "b", "c", "d", "e" , "f", "g","h", "i", "j","k", "l",	"m", "n",	"o" , "p", "r","s","t","u","v", "w",  "x", "y" , "z"]

foreignChracters= [ "@", "#","!","_"]
#--------------------------Random choices---------------------------# 

ranN= random.choice(numbers)
ranN2= random.choice(numbers)
ranN3= random.choice(numbers)
ranN4= random.choice(numbers)


ranL= random.choice(letters)
ranL2= random.choice(letters)
ranL3= random.choice(letters)
ranL4= random.choice(letters)


ransL= random.choice(sLetters)
ransL2= random.choice(sLetters)
ransL3= random.choice(sLetters)
ransL4= random.choice(sLetters)

ranFC= random.choice(foreignChracters)
ranFC2= random.choice(foreignChracters)
ranFC3= random.choice(foreignChracters)
ranFC4= random.choice(foreignChracters)

#---------------------------User Selections----------------------------# 



typeSelection=int(input(" İn this programm you can get randomly passwords. You must make only one thing, choose a type of password you want\nPassword Types:\n1-Password in easy difficulty(8 characters)\n2-Password in medium difficulty (12 characters)\n3-Password in mega difficulty(16 characters)\n\nYour selection: "))
while typeSelection<1 or typeSelection> 3:
      print("-"*50)
      print("Please enter a number between 1 and 3.(Including 1 and 3). Try again.")
      print("-"*50)
      typeSelection=int(input(" İn this programm you can get randomly passwords. You must make only one thing, choose a type of password you want\nPassword Types:\n1-Password in easy difficulty(8 characters)\n2-Password in medium difficulty (12 characters)\n3-Password in mega difficulty(16 characters)\n\nYour selection: "))
if typeSelection== 1:
    print("-"*50)
    print("Your password in easy difficulty:   ")
    print(ransL2+str(ranN2)+ ranFC2+ranFC+str(ranN3)+ ransL3+ ranFC3+ str(ranN))
    print("-"*50)

if typeSelection== 2:
    print("-"*50)
    print("Your password in medium difficulty:")
    print (str(ranN2)+str(ranN3)+ ransL+ ranFC+ ransL2 + ransL2+ ranFC2+ranFC3+ransL3+str(ranN)+ ranL2 +ranL3)
    print("-"*50)
    

if typeSelection== 3:
    print("-"*50)
    print("Your password in mega difficulty:")
    print(ranL2+ransL3+ranFC4+str(ranN3)+str(ranN4)+ str(ranN)+ ransL+ ranFC+ ransL4+ranL3+ ranL4 + str(ranN2)+ ranFC2 + ranFC3 +ranL+ransL2)
    print("-"*50)


#------------------------------------------------------------------------# 