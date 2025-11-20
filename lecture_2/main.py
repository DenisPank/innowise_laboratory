import time # Imported time to determine today's date.

def life_stage(age: int): # Function: int -> str. We assign the profile to a certain age group.
    life_stage = age
    if(life_stage <= 12):
        return "Child"
    if(life_stage <= 19 and life_stage >= 13):
        return "Teenager"
    if(life_stage >= 20):
        return "Adult"
    

def year_age(birth_year: int):
    return time.localtime().tm_year - birth_year  # Function: int -> int. Calculating the age of the profile.

def interface_profile():  # Function: -> dict. The function uses the terminal to query the user about their data. The function does not process incorrect data, errors such as
    name = input("Enter your full name: ")
    birth_year = int(input("Enter your birth year: "))
    hobbies = ''
    list_hobbies = []
    while True:
        hobbies = input("Enter a favorite hobby or type 'stop' to finish: ")
        if hobbies.lower() == 'stop':
            break
        list_hobbies.append(hobbies)
    
    return {"name": name, 
            "age": year_age(birth_year),
            "Life Stage": life_stage(year_age(birth_year)),
            "Favorite Hobbies": list_hobbies, }


def generate_profile(profile: dict[str, any]) -> None:  # Function: dict -> terminal. A function for displaying profile information in a formatted format
    print("\n---")
    print("Profile Summary:")
    print(f"Name: {profile['name']}")
    print(f"Age: {profile['age']}")
    print(f"Life Stage: {profile['Life Stage']}")
    if len(profile['Favorite Hobbies']) > 0:  # Checking the list for a threshold value. If there are no elements, a message will be displayed
        print(f"Favorite Hobbies ({len(profile['Favorite Hobbies'])})")
        for i, value in enumerate(profile['Favorite Hobbies']):
            print(f"- {value}")
    else:
        print("You didn't mention any hobbies.")
    print("---")
    return


generate_profile(interface_profile())

    