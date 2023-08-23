class Link(object):
    
    def __init__(self, string):
        if "|" in string:
            self.link = string[:string.find("|")]
            self.display1 = string[string.find("|") + 1:]
            self.display2 = None
        elif "http" in string:
            self.link = string[:string.find(" ")]
            self.display2 = string[string.find(" ") + 1:]
            self.display1 = None
        else:
            self.link = string
            self.display1 = None
            self.display2 = None
    
    def __str__(self):
        if self.display1:
            return "[[" + str(self.link) + "|" + str(self.display1) + "]]"
        elif self.display2:
            return "[" + str(self.link) + " " + str(self.display2) + "]"
        else:
            return "[[" + str(self.link) + "]]"

    def __repr__(self):
        return str(self)
    
    def url(self):
        url = str(self.link)
        return url if "|" not in url else url[:url.find("|")]
