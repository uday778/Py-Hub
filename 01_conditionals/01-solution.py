age=input("provide me an age: ")

ageInt=int(age)

if ageInt<13:
    print("child")
elif ageInt<20:
    print("teen")
elif ageInt<60:
    print("Adults")
else:
    print("Senior")
