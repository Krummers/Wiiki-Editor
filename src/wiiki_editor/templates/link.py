class Link(object):
    
    def __init__(self, string):
        if string.startswith("[[") and "|" in string:
            self.link = string[2:string.find("|")]
            self.display = string[string.find("|") + 1:-2]
            self.brackets = 2
        elif string.startswith("[["):
            self.link = string[2:-2]
            self.display = None
            self.brackets = 2
        elif string.startswith("["):
            self.link = string[1:string.find(" ")]
            self.display = string[string.find(" ") + 1:-1]
            self.brackets = 1
        else:
            self.link = string
            self.display = None
            self.brackets = 0
    
    def __str__(self):
        if self.brackets == 2 and self.display is None:
            return "[[" + self.link + "]]"
        elif self.brackets == 2 and self.display:
            return "[[" + self.link + "|" + self.display + "]]"
        elif self.brackets == 1:
            return "[" + self.link + " " + self.display + "]"
        else:
            return self.link
    
    def __repr__(self):
        return str(self)