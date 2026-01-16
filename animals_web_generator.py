import json

def load_data(file_path):
    """ Loads JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

for animal in animals_data:
    if 'name' in animal:
        print(f"Name: {animal['name']}")
    if 'diet' in animal:
        print(f"Diet: {animal['diet']}")
    if 'locations' in animal and animal['locations']:
        print(f"Location: {animal['locations'][0]}")
    if 'taxanomy' in animal and "class" in animal['taxanomy']:
        print(f"Type: {animal['taxanomy']['class']}")
    print()