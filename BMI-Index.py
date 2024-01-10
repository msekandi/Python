# BMI-Body Mass Index

height=float(input("Enter the your height: "))
weight=float(input("Enter your weight: "))

BMI =weight/(height**2)
if BMI < 18.5 :
   print("You are under weight")
elif BMI < 25:
   print("You are normal")

elif BMI < 30:
   print("You are overweight")

elif BMI < 35:
   print("You are obese")
elif BMI < 40:
     
else :
  print("You are clinically obese")
Lets break down the code: