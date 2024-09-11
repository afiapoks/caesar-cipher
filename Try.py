def life_in_weeks(age):
    age_in_weeks=(age * 52)
    total_weeks=4680
    remaining_weeks=(total_weeks- age_in_weeks)
    print(f"You have {remaining_weeks} weeks left.")
life_in_weeks(56)
