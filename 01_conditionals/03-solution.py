score=122

if score>=100:
    print("please verify your grade again")
    exit()


if score>=90:
    grade="A"
elif score>=80:
    grade="B"
elif score>=70:
    grade="C"
elif score>=60:
    grade="D"
else:
    grade="F"

print("Grade:",grade)