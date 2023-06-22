import string

def generate_names():
    names = []
    for letter in string.ascii_lowercase:
        name = letter + "name"
        names.append(name)
    return names

all_names = generate_names()

for letter in string.ascii_lowercase:
    filtered_names = list(filter(lambda name: name.startswith(letter), all_names))
    print("Names starting with", letter + ":", filtered_names)
