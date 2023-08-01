import mwclient as mc

class ListCustomTrack(object):
    
    class Table(object):
        
        class Entry(object):
            
            def __init__(self, text):
                pass
        
        def __init__(self, text):
            pass
            
    
    def __init__(self, wiiki):
        self.title = "List of Custom Tracks"
        self.object = mc.page.Page(wiiki, self.title)
        text = self.object.text()
        
        self.top = text[:text.find("== Overview ==") - 1].split("\n")
        self.overview = text[text.find("== Overview ==") + len("== Overview ==") + 1:text.find("== Track List ==") - 1]
        self.table = text[text.find("== Track List ==") + len("== Track List ==") + 1:text.find("== Translations ==") - 1]
        self.translations = text[text.find("== Translations ==") + len("== Translations ==") + 1:text.rfind("\n\n[[") + 1]
        self.bottom = text[text.rfind("\n\n[[") + len("\n\n[[") - 2:].split("\n")
