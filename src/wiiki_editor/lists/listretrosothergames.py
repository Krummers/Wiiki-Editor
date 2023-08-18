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
        
        i = 0
        while True:
            next_separator = "|-\n" if i % 2 != 0 else "|- class=alt\n"
            self_separator = "|-\n" if i % 2 == 0 else "|- class=alt\n"
            
            first_piece = text[:text.find("]]")]
            if "data-sort-value" in first_piece and "rowspan" in first_piece:
                # not present in list, fabricate it
                sort = first_piece[first_piece.find("\"") + 1:first_piece.rfind("\"")]
                text = text.replace(" data-sort-value=\"" + sort + "\"", "")
                rows = int(text[len("| rowspan=")])
                title = text[text.find("[["):text.find("]]") + 2]
                text = text[text.find("\n") + 1:]
                authors = []
                firsts = []
                latests = []
                for x in range(rows):
                    column = text[2:text.find("\n|")].split(" || ")
                    authors.append(column[0])
                    firsts.append(column[1])
                    latests.append(column[2])
                    if x < rows - 1:
                        text = text[text.find("|-") + 3:]
                entry = Entry(title, authors, firsts, latests, rows, sort)
            elif "data-sort-value" in first_piece:
                column = text[2:text.find("\n|-")].split("\n| ")
                sort = column[0][column[0].find("\"") + 1:column[0].rfind("\"")]
                title = column[0][column[0].rfind("|") + 1:-2]
                prefix = column[0][column[0].find("[[") + 2:column[0].find(title) - 1]
                entry = Entry(title, prefix, column[1], column[2], column[3], column[4], 1, sort)
            elif "rowspan" in first_piece:
                # needs to be done
                rows = int(text[len("| rowspan=")])
                title = first_piece[first_piece.rfind("|") + 1:]
                prefix = first_piece[first_piece.find("[[") + 2:first_piece.find(title) - 1]
                text = text[text.find("\n") + 1:]
                second_piece = text[:text.find("\n")]
                if "data-sort-value" in second_piece:
                    game = second_piece[second_piece.find("data-sort-value"):]
                else:
                    game = second_piece[second_piece.find("''"):]
                text = text[text.find("\n") + 1:]
                authors = []
                firsts = []
                latests = []
                for x in range(rows):
                    if x < rows - 1:
                        column = text[2:text.find(self_separator) - 1].split("\n| ")
                    else:
                        column = text[2:text.find(next_separator) - 1].split("\n| ")
                    authors.append(column[0])
                    firsts.append(column[1])
                    latests.append(column[2])
                    if x < rows - 1:
                        text = text[text.find(self_separator) + len(self_separator):]
                entry = Entry(title, prefix, game, authors, firsts, latests, rows)
            else:
                column = text[2:text.find("\n|-")].split("\n| ")
                title = column[0][column[0].find("|") + 1:-2]
                prefix = column[0][2:column[0].find(title) - 1]
                entry = Entry(title, prefix, column[1], column[2], column[3], column[4])
            
            self.entries.append(entry)
            
            if text.find("|-") == -1:
                break
            
            text = text[text.find(next_separator) + len(next_separator):]
            i += 1
        
        self.entries[-1].latest = self.entries[-1].latest[:-3]
    
    def __str__(self):
        string = "\n".join(self.classification)
        for entry, x in zip(self.entries, range(len(self.entries))):
            if x % 2 == 0:
                string += "|-\n" + str(entry)
            else:
                string += "|- class=alt\n" + entry.__str__(True)
        string += "|}\n"
        return string
    
    def __repr__(self):
        return "Retro Tracks from Non-Mario Kart Games table with {} entries".format(len(self.entries))
    
    def __add__(self, other):
        if type(other) != Entry:
            raise TypeError("only objects of type 'Entry' are supported")
        result = Table(str(self))
        for entry in result.entries:
            if entry.title == other.title:
                if entry.rowspan > 1:
                    entry.author.append(other.author)
                    entry.first.append(other.first)
                    entry.latest.append(other.latest)
                else:
                    entry.author = [entry.author, other.author]
                    entry.first = [entry.first, other.first]
                    entry.latest = [entry.latest, other.latest]
                entry.rowspan += 1
                return result
        result.entries.append(other)
        result.sort()
        return result
    
    def update_release(self, track, date, author = None):
        for entry in self.entries:
            if entry.prefix + " " + entry.title == track:
                if entry.rowspan > 1:
                    position = entry.author.index(author)
                    entry.latest[position] = date
                else:
                    entry.latest = date
                break
    
    def sort(self):
        self.entries = sorted(self.entries, key = lambda entry:entry.sortstring)

class Entry(object):
    
    def __init__(self, title, prefix, game, author, first, latest, rowspan = 1, sort = None):
        self.title = title
        self.prefix = prefix
        self.game = game
        self.author = author
        self.first = first
        self.latest = latest
        self.rowspan = rowspan
        self.sort = sort if sort else title
        self.sortstring = sort_string(self.sort)
    
    def __str__(self, special_separator = False):
        if self.sort != self.title and self.rowspan > 1:
            raise NotImplementedError("this type does not exist in the table yet")
        elif self.sort != self.title:
            string = "| data-sort-value=\"" + str(self.sort) + "\"| "
            string += "[[" + str(self.prefix) + " " + str(self.title) + "|" + str(self.title) + "]]\n"
            string += "| " + str(self.game) + "\n"
            string += "| " + str(self.author) + "\n"
            string += "| " + str(self.first) + "\n"
            string += "| " + str(self.latest) + "\n"
        elif self.rowspan > 1:
            string = "| rowspan=" + str(self.rowspan) + "| "
            string += "[[" + str(self.prefix) + " " + str(self.title) + "|" + str(self.title) + "]]\n"
            string += "| rowspan=" + str(self.rowspan)
            if "data-sort-value" in self.game:
                string += " " + str(self.game) + "\n"
            else:
                string += "| " + str(self.game) + "\n"
            for x in range(self.rowspan):
                string += "| " + str(self.author[x]) + "\n"
                string += "| " + str(self.first[x]) + "\n"
                string += "| " + str(self.latest[x]) + "\n"
                if x < self.rowspan - 1:
                    if special_separator:
                        string += "|- class=alt\n"
                    else:
                        string += "|-\n"
        else:
            string = "| [[" + str(self.prefix) + " " + str(self.title) + "|" + str(self.title) + "]]\n"
            string += "| " + str(self.game) + "\n"
            string += "| " + str(self.author) + "\n"
            string += "| " + str(self.first) + "\n"
            string += "| " + str(self.latest) + "\n"
        
        return string
    
    def __repr__(self):
        representation = ""
        representation += "Title: " + str(self.prefix) + " " + str(self.title) + "\n"
        representation += "Game: " + str(self.game) + "\n"
        representation += "Author(s): " + str(self.author) + "\n"
        representation += "First: " + str(self.first) + "\n"
        representation += "Latest: " + str(self.latest)
        if self.rowspan > 1:
            representation += "\nRowspan of " + str(self.rowspan)
        if self.sort != self.title:
            representation += "\nData sort value: " + str(self.sort)
        return representation
