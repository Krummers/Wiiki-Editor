import mwclient as mc

class ListCustomTracks(object):
    
    def __init__(self, wiiki):
        self.title = "List of Custom Tracks"
        self.object = mc.page.Page(wiiki, self.title)
        text = self.object.text()
        
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
        return "List of Custom Tracks article"

class Table(object):
    
    def __init__(self, text):
        class_pos = text.find("|-")
        self.classification = text[:class_pos].split("\n")
        text = text[class_pos + 3:]
        self.entries = []
        
        while True:
            first_piece = text[:text.find("]]")]
            if "data-sort-value" in first_piece and "rowspan" in first_piece:
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
                column = text[2:text.find("\n|")].split(" || ")
                sort = column[0][column[0].find("\"") + 1:column[0].rfind("\"")]
                title = column[0][column[0].find("[["):column[0].find("]]") + 2]
                entry = Entry(title, column[1], column[2], column[3], 1, sort)
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
                entry.author.append(other.author)
                entry.first.append(other.first)
                entry.latest.append(other.append)
                entry.rowspan += 1
                return result
        result.entries.append(other)
        result.entries = sorted(result.entries, key = lambda entry:entry.sort \
                  if entry.sort.startswith("[[") else "[[" + entry.sort + "]]")
        return result

class Entry(object):
    
    def __init__(self, title, author, first, latest, rowspan = 1, sort = None):
        self.title = title
        self.author = author
        self.first = first
        self.latest = latest
        self.rowspan = rowspan
        if sort:
            self.sort = sort
        else:
            self.sort = title
    
    def __str__(self):
        if self.sort != self.title and self.rowspan > 1:
            string = "| data-sort-value=\"" + str(self.sort) + "\""
            string += " rowspan=" + str(self.rowspan) + "| "
            string += str(self.title) + "\n"
            for x in range(self.rowspan):
                string += "| " + str(self.author[x]) + " || "
                string += str(self.first[x]) + " || "
                string += str(self.latest[x]) + "\n"
                if x < self.rowspan - 1:
                    string += "|-\n"
        elif self.sort != self.title:
            string = "| data-sort-value=\"" + str(self.sort) + "\"| "
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
        if self.sort != self.title:
            representation += "\nData sort value: " + str(self.sort)
        return representation
