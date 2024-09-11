def greet():
    print("Hello")
    print("How are you?")
    print("Have a great day!")
greet()

#functions that allows inputs
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you? {name}")
    print(f"Have a great day! {name}")
greet_with_name("Afia")

age=input("How old are you? ")

age_in_weeks=(age * 52)
total_weeks=4680
remaining_weeks=(total_weeks- age_in_weeks)

def life_in_weeks(remaining_weeks):
    age=input("How old are you? ")
    age_in_weeks=(age * 52)
    total_weeks=4680
    remaining_weeks=(total_weeks- age_in_weeks)
    print(f"You have {remaining_weeks} weeks left.")
life_in_weeks(remaining_weeks)

'''
def life_in_weeks(age):
    years_remaining=90-age
    weeks_remaining=years_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")

life_in_weeks(56)
'''