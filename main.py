name = "Michaela"
name2 = "Sylvester"
age = 21 #Declared a int

age2 = "21" # Example of another str

number1 = 34
number2 = 56543

#print(number1 + number2)

number3 = 23.4 #Declaring a float
print(name)
print(name2)
print(age2)
print(name,name2,age2)

human_age = 6 #I picked this age
dog_age = 7 #one human year is seven dog years
human_in_dog_years = human_age * dog_age
print("An age" ,human_age , "human should be" , human_in_dog_years, "in dogs age."
     )

human_age = 45 #I picked this age
cat_age = 9
human_in_cat_age = human_age / cat_age
print("An age" ,human_age, "human should be", human_in_cat_age,"in cat age.")

human_age = 12
horse_years = 3 * ((((human_age ** 2) - 47)/7)+12)
print("An age" , human_age, "human should be" , horse_years, "in horse years.")

first_name = str(input("What is your first name?"))
last_name = str(input("What is your last name?"))
age = int(input("What is your age?"))

print(age * 35)


human_age = 2.1
dog_age = 7
human_in_dog_years = human_age * dog_age

number_of_days = human_in_dog_years * 365

years =  number_of_days // 365
months = (number_of_days - years * 365) // 30
days = round(number_of_days - years* 365 - months*30)


print("An age" , human_age , "human should be", years, "years", months , "months" , days , "days in dog years.")


human_age = 21.6
cat_age = 2.4
human_in_cat_years = human_age / cat_age

number_of_days = human_in_cat_years * 365

years =  number_of_days // 365
months = (number_of_days - years * 365) // 30
days = round(number_of_days - years* 365 - months*30)

print("An age" , human_age , "human should be", years, "years", months , "months" , days , "days in cat years.")


human_age = 12
horse_years = 3 * ((((human_age ** 2) - 47)/7)+12)
human_in_horse_years = human_age * horse_years
number_of_days = human_in_horse_years * 365
print("An age" , human_age , "human should be", years, "years", months , "months" , days , "days in horse years.")