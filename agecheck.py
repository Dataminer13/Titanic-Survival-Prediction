name=input("What is your name? ")
age=int(input("How old are you? "))

yearsto50=50-age

if yearsto50>0:
    print(""+name+", you'll be 50 in "+str(yearsto50)+" years.")
else:
    print(""+name+", you were 50 prevously "+str(-yearsto50)+" years ago.")

print("Thanks")