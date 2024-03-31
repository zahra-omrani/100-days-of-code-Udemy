weight = input("Enter your weight:\n")
height = input("Enter your height:\n")
BMI = int(int(weight)/(float(height))**2)
print(f"Your BMI is {BMI}")
if BMI <= 18.5:
    print("you are under weight")
elif BMI > 18.5 and BMI <= 25:
    print("you have a normal weight") 
elif BMI > 25 and BMI <= 30:
    print("you are overweight")
elif BMI > 30 and BMI <= 35:
    print("you are obese")
else :
    print("you are clinically obese") 