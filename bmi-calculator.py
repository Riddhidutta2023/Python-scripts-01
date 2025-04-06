#this script asks 
#for the user's height and weight, then calculates and displays their BMI
#BMI = weight (kg) / height (m)^2

user_weight = float(input("Enter your weight in kg: "))
user_height = float(input("Enter your height in meters: "))
# Calculate BMI
bmi = user_weight / (user_height ** 2)
# Display the result
print(f"Your BMI is: {bmi:.2f}")