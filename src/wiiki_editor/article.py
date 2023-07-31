import mwclient as mc

class Article(object):
    
    def __init__(self, title, wiiki):
        self.title = title
        self.object = mc.page.Page(wiiki, title)
        self.text = self.object.text()
        
        if self.text.startswith("#REDIRECT [["):
            self.title = self.text[12:-2]
            self.object = mc.page.Page(wiiki, self.title)
            self.text = self.object.text()