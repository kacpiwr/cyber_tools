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

def recursive_password_generation(current_temp, data, index, passlist_file, password):

    if current_temp[index] == "" or index >= len(current_temp):
        passlist_file.write(password + '\n')
        return
    if current_temp[index] == "name":
        for name in data["names"]:
            current_password = password + str(name)
            recursive_password_generation(current_temp, data, index + 1, passlist_file, current_password)
            return
    if current_temp[index] == "sur":
        for surname in data["surnames"]:
            current_password = password + str(surname)
            recursive_password_generation(current_temp, data, index + 1, passlist_file, current_password)
            return
    if current_temp[index] == "city":
        for city in data["cities"]:
            current_password = password + str(city)
            recursive_password_generation(current_temp, data, index + 1, passlist_file, current_password)
            return
    if current_temp[index] == "animal":
        for animal in data["animals"]:
            current_password = password + str(animal)
            recursive_password_generation(current_temp, data, index + 1, passlist_file, current_password)
            return
    if current_temp[index] == "special_thing":
        for special_thing in data["special_things"]:
            current_password = password + str(special_thing)
            recursive_password_generation(current_temp, data, index + 1, passlist_file, current_password)
            return
    if current_temp[index] == "number":
        for number in data["numbers"]:
            current_password = password + str(number)
            recursive_password_generation(current_temp, data, index + 1, passlist_file, current_password)
            return
    if current_temp[index] == "day":
        for fdate in data["dates"]:
            day_variation = get_date_variations(fdate, "daydaymounth")
            current_password = password + str(day_variation)
            recursive_password_generation(current_temp, data, index + 1, passlist_file, current_password)
        return
    if current_temp[index] == "mounth":
        for fdate in data["dates"]:
            mounth_variation = get_date_variations(fdate, "mounthday")
            current_password = password + str(mounth_variation)
            recursive_password_generation(current_temp, data, index + 1, passlist_file, current_password)
        return
    if current_temp[index] == "year":
        for fdate in data["dates"]:
            year_variation = get_date_variations(fdate, "yearmounthyear")
            current_password = password + str(year_variation)
            recursive_password_generation(current_temp, data, index + 1, passlist_file, current_password)
        return

        


def create_passlist_with_combinations():
    with open('/Users/kacperwrobel/Documents/cyber_tools/json_files/templates.json', 'r') as file:
        templates = json.load(file)

    with open('/Users/kacperwrobel/Documents/cyber_tools/json_files/data_for_templates.json', 'r') as file:
        data = json.load(file)

    passlist_file = open('/Users/kacperwrobel/Documents/cyber_tools/password_files/passlist.txt', 'w', encoding='utf-8')
    passwords=[]
    i = 1
    current_temp = []
    for template in templates["templates"]:
        print(f"Processing template: {i}")
        i += 1
        current_temp = template.split("_")
        print(current_temp)
        recursive_password_generation(current_temp, data, 0, passlist_file, "")

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
    
    with open('/Users/kacperwrobel/Documents/cyber_tools/json_files/data_for_templates.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    
    create_passlist_with_combinations()



if __name__ == "__main__":
    create_passlist_with_combinations()