import functions
        
print("…………………………………………………………………………………………………………………………………………|")
print("😃😃😃 Welcome in my first python application 😃😃😃|")
print("…………………………………………………………………………………………………………………………………………|")

st=input("Enter ---(regs) --- For Registration Or Enter --- (login) --- For login ➡➡➡➡ \n………………………………………………………………………………………………………………………………………………………………………………………………………………\n")

while not functions.is_alpha(st) or not functions.have_value(st):
    print("Please Enter your choise")
    st=input("Enter ---(regs) --- For Registration Or Enter --- (login) --- For login ➡➡➡➡ 		  	      \n………………………………………………………………………………………………………………………………………………………………………………………………………………\n")


if st=="regs":
     functions.Form_User()

elif st=="login":
    functions.login()
