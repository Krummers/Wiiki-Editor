import importlib as il

characters = il.resources.files("wiiki_editor").joinpath("sort.txt").read_text("utf-8")
characters = characters.split("\n")

def sort_string(string):
    sort_string = ""
    for letter in string.lower():
        sort_string += chr(characters.index(letter))
    return sort_string
