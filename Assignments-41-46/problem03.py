# Input Example 38
age = input("Inter age : ").strip()
age = int(age)
print(type(age))
if((age>10) and (age <100)):
    months = age *12
    weeks = months * 4
    days = age * 365
    hours = days * 24
    minutes= hours *60
    seconds = minutes * 60

    print("Are You need Your Age By Months (M): ") 
    print("Are You need Your Age By Weeks  (W): ") 
    print("Are You need Your Age By Days (D) : ") 
    print("Are You need Your Age By Hours (H) : ") 
    print("Are You need Your Age By Minutes (Mi) : ") 
    print("Are You need Your Age By Seconds  (S) : ") 

    convertAge = input("Inter period: ").strip().lower() 
    if(convertAge == "months" or convertAge == "m"): print(f"Your Age In Months Is {months:,} Months") 
    elif(convertAge == "weeks" or convertAge == "w"): print(f"Your Age In Weeks Is {weeks:,} Weeks") 
    elif(convertAge == "days" or convertAge == "d"): print(f"Your Age In Days Is {days:,} Days") 
    elif(convertAge == "hours" or convertAge == "h"): print(f"Your Age In Hours Is {hours:,} Hours") 
    elif(convertAge == "minutes" or convertAge == "mi"): print(f"Your Age In Minutes Is {minutes:,} Minutes") 
    elif(convertAge == "seconds" or convertAge == "s"): print(f"Your Age In Seconds Is {seconds:,} Seconds") 
else:
    print("age exite in interval")
# Needed Output
"Your Age In Months Is 456 Months" # Months Example
"Your Age In Weeks Is 1824 Weeks" # Weeks Example