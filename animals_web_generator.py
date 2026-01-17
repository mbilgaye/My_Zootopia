import json

def load_data(file_path):
    """ Loads JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def read_template(file_path):
    """Reads an HTML template file and returns it as a string"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()

def build_animals_string(animals_data):
    output = ""

    for animal in animals_data:
        output += '<li class="cards_item">\n'

        if 'name' in animal:
            output += f"Name: {animal['name']}<br/>\n"

        if 'characteristics' in animal and "diet" in animal['characteristics']:
            output += f"Diet: {animal['characteristics']['diet']}<br/>\n"

        if 'locations' in animal and animal['locations']:
            output += f"Location: {(animal['locations'][0])}<br/>\n"

        if 'characteristics' in animal and "type" in animal['characteristics']:
            output += f"Type: {animal['characteristics']['type']}<br/>\n"

        output += "</li>"
    return output

def write_html_file(file_path, content):
    """Writes the final HTML content to a file"""
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(content)

animals_data = load_data("animals_data.json")
template = read_template("animals_template.html")

animals_output = build_animals_string(animals_data)

new_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_output)

write_html_file("animals.html", new_html)
print("animals.html generated successfully!")