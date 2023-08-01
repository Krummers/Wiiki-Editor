import mwclient as mc

class Article(object):
    
    def __init__(self, title, wiiki):
        self.title = title
        self.object = mc.page.Page(wiiki, title)
        self.text = self.object.text()
