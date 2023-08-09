from ..article import Article
from ..sortstring import sort_string

class ListRetrosOtherGames(object):
    
    def __init__(self, wiiki):
        self.title = "List of Retro Tracks from Non-Mario Kart Games"
        text = Article(self.title, wiiki).text
        
        self.templates = text[:text.find("This is a") - 1].split("\n")
        self.overview = text[text.find("This is a"):text.find("{| class") - 1]
        self.tracks = Table(text[text.find("{| class"):text.find("|}\n\n{|") + len("|}\n")])
        self.arenas = Table(text[text.rfind("{| class"):text.rfind("|}") + 3])
        self.categories = text[text.rfind("\n\n[[") + len("\n\n[[") - 2:].split("\n")
    
    def __str__(self):
        string = "\n".join(self.templates)
        string += "\n" + str(self.overview)
        string += "\n" + str(self.tracks)
        string += "\n" + str(self.arenas)
        string += "\n" + "\n".join(self.categories) + "\n"
        return string
    
    def __repr__(self):
        return str(self.title) + " article"

class Table(object):
    
    def __init__(self, text):
        class_pos = text.find("|-")
        self.classification = text[:class_pos].split("\n")
        text = text[class_pos + 3:]
        self.entries = []

class Entry(object):
    
    def __init__(self, title, game, link, author, first, latest, rowspan = 1, sort = None):
        pass
