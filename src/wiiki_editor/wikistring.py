import importlib as il

characters = il.resources.files("wiiki_editor").joinpath("Sort.txt").read_text("utf-8")
characters = characters.split("\n")
characters.append("꿈")
characters.append("★")
characters.append("\u200e")

class WikiString(object):
    
    def __init__(self, string):
        wiki = ""
        for letter in string.lower():
            wiki += chr(characters.index(letter))
        self.wiki = wiki
        self.string = str(string)
    
    def __str__(self):
        return self.string
    
    def __repr__(self):
        return self.wiki + "\n" + self.string
    
    def __lt__(self, other):
        if type(other) != WikiString:
            raise TypeError("only objects of type 'WikiString' are supported")
        return self.wiki < other.wiki
    
    def __le__(self, other):
        if type(other) != WikiString:
            raise TypeError("only objects of type 'WikiString' are supported")
        return self == other or self < other
    
    def __eq__(self, other):
        if type(other) != WikiString:
            raise TypeError("only objects of type 'WikiString' are supported")
        if self.wiki == other.wiki:
            return True
        else:
            return False
    
    def __gt__(self, other):
        if type(other) != WikiString:
            raise TypeError("only objects of type 'WikiString' are supported")
        return self.wiki > other.wiki
    
    def __ge__(self, other):
        if type(other) != WikiString:
            raise TypeError("only objects of type 'WikiString' are supported")
        return self == other or self > other
    
    def __ne__(self, other):
        if type(other) != WikiString:
            raise TypeError("only objects of type 'WikiString' are supported")
        if self.wiki != other.wiki:
            return True
        else:
            return False
    
    def __len__(self):
        return len(self.wiki)
