import json
from datetime import date

def get_date_variations(passed_date, format_type):
    # Assuming passed_date is compatible with your date() constructor
    passed_date_var = date.fromisoformat(passed_date) 
    str_date = ""
    
    if(format_type == "daymounth"):
        str_date = str(passed_date_var.day) + str(passed_date_var.month)
    elif(format_type == "mounthday"):
        str_date = str(passed_date_var.month) + str(passed_date_var.day)
    elif(format_type == "daydaymounth"):
        str_date = str(passed_date_var.day).zfill(2) + str(passed_date_var.month)
    elif(format_type == "daydaymounthyear"):
        str_date = str(passed_date_var.day).zfill(2) + str(passed_date_var.month) + str(passed_date_var.year)
    elif(format_type == "daymounthyear"):
        str_date = str(passed_date_var.day) + str(passed_date_var.month) + str(passed_date_var.year)
    elif(format_type == "yearmounth"):
        str_date = str(passed_date_var.year) + str(passed_date_var.month)
    elif(format_type == "yearmounthyear"):
        # Literal interpretation of the string provided
        str_date = str(passed_date_var.year) + str(passed_date_var.month) + str(passed_date_var.year)

    return str_date

def create_passlist_with_combinations():
    with open('templates.json', 'r') as file:
        templates = json.load(file)

    with open('data_for_templates.json', 'r') as file:
        data = json.load(file)

    passlist_file = open('passlist.txt', 'w', encoding='utf-8')
    passwords=[]
    i = 1
    for template in templates["templates"]:
        print(f"Processing template: {i}")
        i += 1
        for  name in data["names"]:
            for animal in data["animals"]:
                for city in data["cities"]:
                    for surname in data["surnames"]:
                        for special_thing in data["special_things"]:
                            for number in data["numbers"]:
                                for fdate in data["dates"]:
                                    password = template
                                    password = password.replace("name", name)
                                    password = password.replace("sur", surname)
                                    password = password.replace("city", city)
                                    password = password.replace("animal", animal)
                                    password = password.replace("special_thing", special_thing)
                                    password = password.replace("number", str(number))
                                    password = password.replace("day", str(date.fromisoformat(fdate).day))
                                    password = password.replace("year", str(date.fromisoformat(fdate).year))
                                    password = password.replace("mounth", str(date.fromisoformat(fdate).month))

                                    # if password not in passwords:
                                    passlist_file.write(password + '\n')
                                    passwords.append(password)
    passlist_file.close()

def input_data_for_templates():
    data = {
        "names": [],
        "surnames": [],
        "cities": [],
        "animals": [],
        "special_things": [],
        "numbers": [],
        "dates": []
    }
    print("Provide data for templates in JSON format:")
    print("Names: ")
    k="init"
    while k!="":
        k = input().strip()
        if k!="":
            data["names"].append(k)
    print("Surnames:")
    k="init"
    while k!="":
        k = input().strip()
        if k!="":
            data["surnames"].append(k)
    print("Cities:")
    k="init"
    while k!="":
        k = input().strip()
        if k!="":
            data["cities"].append(k)
    print("Animals:")
    k="init"
    while k!="":
        k = input().strip()
        if k!="":
            data["animals"].append(k)
    print("Special things:")
    k="init"
    while k!="":
        k = input().strip()
        if k!="":
            data["special_things"].append(k)
    print("Numbers:")
    k="init"
    while k!="":
        k = input().strip()
        if k!="":
            data["numbers"].append(int(k))
    print("Dates (in format YYYY-MM-DD):")
    k="init"
    while k!="":
        k = input().strip()
        if k!="":
            data["dates"].append(k)
    
    with open('data_for_templates.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    
    create_passlist_with_combinations()



if __name__ == "__main__":
    create_passlist_with_combinations()