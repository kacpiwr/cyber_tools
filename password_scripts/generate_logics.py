import json

def generate_templates():
    # Lista elementów (kategorii) w liczbie pojedynczej
    elements = [
        "name_",
        "city_",
        "surname_",
        "animal_",
        "specialThing_",
        "number_",
        "day_",
        "mounth_",
        "year_"
    ]

    templates = []

    print("Generating 2-element templates/Users/kacperwrobel/Documents/cyber_tools.")
    for element1 in elements:
        for element2 in elements:
            password = f"{element1}{element2}"
            if password not in templates:
                templates.append(password)

    print("Generating 3-element templates/Users/kacperwrobel/Documents/cyber_tools.")
    for element1 in elements:
        for element2 in elements:
            for element3 in elements:
                password = f"{element1}{element2}{element3}"
                if password not in templates:
                    templates.append(password)

    print("Generating 4-element templates/Users/kacperwrobel/Documents/cyber_tools.")
    for element1 in elements:
        for element2 in elements:
            for element3 in elements:
                for element4 in elements:
                    password = f"{element1}{element2}{element3}{element4}"
                    if password not in templates:
                        templates.append(password)

    print("Generating 5-element templates/Users/kacperwrobel/Documents/cyber_tools.")
    for element1 in elements:
        for element2 in elements:
            for element3 in elements:
                for element4 in elements:
                    for element5 in elements:
                        password = f"{element1}{element2}{element3}{element4}{element5}"
                        if password not in templates:
                            templates.append(password)
    

    result = {
        "templates": templates
    }


    with open('/Users/kacperwrobel/Documents/cyber_tools/json_files/templates.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4)

    print(json.dumps(result, indent=4))
    print(f"\nWygenerowano {len(templates)} szablonów.")

if __name__ == "__main__":
    generate_templates()