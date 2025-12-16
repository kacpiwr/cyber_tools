import json

def generate_templates():
    # Lista elementów (kategorii) w liczbie pojedynczej
    elements = [
        "name",
        "city",
        "surname",
        "animal",
        "special_thing",
        "number",
        "day",
        "mounth",
        "year"
    ]

    templates = []

    print("Generating 2-element templates...")
    for element1 in elements:
        for element2 in elements:
            password = f"{element1}{element2}"
            if password not in templates:
                templates.append(password)

    print("Generating 3-element templates...")
    for element1 in elements:
        for element2 in elements:
            for element3 in elements:
                password = f"{element1}{element2}{element3}"
                if password not in templates:
                    templates.append(password)

    print("Generating 4-element templates...")
    for element1 in elements:
        for element2 in elements:
            for element3 in elements:
                for element4 in elements:
                    password = f"{element1}{element2}{element3}{element4}"
                    if password not in templates:
                        templates.append(password)

    print("Generating 5-element templates...")
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


    with open('templates.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4)

    print(json.dumps(result, indent=4))
    print(f"\nWygenerowano {len(templates)} szablonów.")

if __name__ == "__main__":
    generate_templates()