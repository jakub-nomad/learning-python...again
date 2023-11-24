from datetime import *
today = date.today()
birthdayHappened = False
minYear = 1900
maxYear = today.year-1
minMonth = 1
maxMonth = 12
minDate = 1
maxDate = 31
userYearBirth = 0
userMonthBirth = 0
userDayBirth = 0

def setBirthDate():
    global userYearBirth
    global userMonthBirth
    global userDayBirth
    try:
        loop = True
        while loop == True:
            userYearBirth = int(input("Enter your year of birth: "))
            while userYearBirth > maxYear or userYearBirth < minYear:
                userYearBirth = int(input("Please enter a valid year of birth: "))

            userMonthBirth = int(input("Enter your month of birth as a number: "))
            while userMonthBirth > maxMonth or userMonthBirth < minMonth:
                userMonthBirth = int(input("Please enter a valid month of birth as a number: "))

            userDayBirth = int(input("Enter your day of birth: "))
            while userDayBirth > maxDate or userDayBirth < minDate:
                userDayBirth = int(input("Please enter a valid day of birth: "))
            loop = False
    except ValueError:
            setBirthDate()

setBirthDate()

if userMonthBirth < today.month:
    birthdayHappened = True
elif userMonthBirth == today.month:
    if userDayBirth >= today.day:
        birthdayHappened = True
    else:
        birthdayHappened = False
else:
    birthdayHappened = False

if birthdayHappened == True:
    print(f"You are {today.year-userYearBirth} years old!")
else:
    print(f"You are {today.year-userYearBirth-1} years old!")