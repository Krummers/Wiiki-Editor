from ..article import Article
from ..templates.link import Link
from ..sortstring import sort_string

class ListCustomTracks(object):
    
    def __init__(self, wiiki):
        self.title = "List of Custom Tracks"
        text = Article(self.title, wiiki).text
        
        self.templates = text[:text.find("== Overview ==") - 1].split("\n")
        self.overview = text[text.find("== Overview ==") + len("== Overview ==") + 1:text.find("== Track List ==") - 1]
        self.table = Table(text[text.find("== Track List ==") + len("== Track List ==") + 1:text.find("== Translations ==") - 1])
        self.translations = text[text.find("== Translations ==") + len("== Translations ==") + 1:text.rfind("\n\n[[") + 1]
        self.categories = text[text.rfind("\n\n[[") + len("\n\n[[") - 2:].split("\n")
    
    def __str__(self):
        string = "\n".join(self.templates)
        string += "\n== Overview ==\n" + str(self.overview)
        string += "\n== Track List ==\n" + str(self.table)
        string += "\n== Translations ==\n" + str(self.translations)
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
        
        while True:
            first_piece = text[:text.find("]]")]
            if "data-sort-value" in first_piece and "rowspan" in first_piece:
                data_sort = first_piece[first_piece.find("\"") + 1:first_piece.rfind("\"")]
                text = text.replace(" data-sort-value=\"" + data_sort + "\"", "")
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
                entry = Entry(title, authors, firsts, latests, rows, data_sort)
            elif "data-sort-value" in first_piece:
                column = text[2:text.find("\n|")].split(" || ")
                data_sort = column[0][column[0].find("\"") + 1:column[0].rfind("\"")]
                title = column[0][column[0].find("[["):column[0].find("]]") + 2]
                entry = Entry(title, column[1], column[2], column[3], 1, data_sort)
            elif "rowspan" in first_piece:
                rows = int(text[len("| rowspan=")])
                title = text[text.find("[["):text.find("]]") + 2]
                text = text[text.find("\n") + 1:]
                authors = []
                firsts = []
                latests = []
                for x in range(rows):
                    column = text[2:text.find("\n")].split(" || ")
                    authors.append(column[0])
                    firsts.append(column[1])
                    latests.append(column[2])
                    if x < rows - 1:
                        text = text[text.find("|-") + 3:]
                entry = Entry(title, authors, firsts, latests, rows)
            else:
                column = text[2:text.find("\n|")].split(" || ")
                entry = Entry(column[0], column[1], column[2], column[3])
            
            self.entries.append(entry)
            
            if text.find("\n") == text[:-1].rfind("\n"):
                break
            
            text = text[text.find("|-") + 3:]
    
    def __str__(self):
        string = "\n".join(self.classification)
        for entry in self.entries:
            string += "|-\n" + str(entry)
        string += "|}\n"
        return string
    
    def __repr__(self):
        return "Custom Track Table with {} entries".format(len(self.entries))
    
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
    
    def update_release(self, title, date, author = None):
        for entry in self.entries:
            if entry.title == title:
                if entry.rowspan > 1:
                    position = entry.author.index(author)
                    entry.latest[position] = date
                else:
                    entry.latest = date
                break
    
    def sort(self):
        self.entries = sorted(self.entries, key = lambda entry:entry.sortstring)

class Entry(object):
    
    def __init__(self, title, author, first, latest, rowspan = 1, data_sort = None):
        self.title = Link(title)
        self.author = author
        self.first = first
        self.latest = latest
        self.rowspan = rowspan
        self.data_sort = data_sort if data_sort else self.title.link
        self.sortstring = sort_string(self.data_sort)
    
    def __str__(self):
        if self.data_sort != self.title.link and self.rowspan > 1:
            string = "| data-sort-value=\"" + str(self.data_sort) + "\""
            string += " rowspan=" + str(self.rowspan) + "| "
            string += str(self.title) + "\n"
            for x in range(self.rowspan):
                string += "| " + str(self.author[x]) + " || "
                string += str(self.first[x]) + " || "
                string += str(self.latest[x]) + "\n"
                if x < self.rowspan - 1:
                    string += "|-\n"
        elif self.data_sort != self.title.link:
            string = "| data-sort-value=\"" + str(self.data_sort) + "\"| "
            string += str(self.title) + " || "
            string += str(self.author) + " || "
            string += str(self.first) + " || "
            string += str(self.latest) + "\n"
        elif self.rowspan > 1:
            string = "| rowspan=" + str(self.rowspan) + "| "
            string += str(self.title) + "\n"
            for x in range(self.rowspan):
                string += "| " + str(self.author[x]) + " || "
                string += str(self.first[x]) + " || "
                string += str(self.latest[x]) + "\n"
                if x < self.rowspan - 1:
                    string += "|-\n"
        else:
            string = "| "
            string += str(self.title) + " || "
            string += str(self.author) + " || "
            string += str(self.first) + " || "
            string += str(self.latest) + "\n"
        
        return string
    
    def __repr__(self):
        representation = ""
        representation += "Title: " + str(self.title) + "\n"
        representation += "Author(s): " + str(self.author) + "\n"
        representation += "First: " + str(self.first) + "\n"
        representation += "Latest: " + str(self.latest)
        if self.rowspan > 1:
            representation += "\nRowspan of " + str(self.rowspan)
        if self.data_sort != self.title:
            representation += "\nData sort value: " + str(self.data_sort)
        return representation
