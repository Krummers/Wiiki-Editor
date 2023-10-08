import mwclient as mc

from .article import Article
from .lists.listcustomtracks import ListCustomTracks, Table as LCTTable, Entry as LCTEntry
from .lists.listretrosothergames import ListRetrosOtherGames, Table as LROGTable, Entry as LROGEntry

class Wiiki(object):
    
    def __init__(self, username, password, api):
        wiiki = mc.Site("wiki.tockdom.com", custom_headers = {"User-Agent": api})
        wiiki.login(username, password)
        self.wiiki = wiiki
        self.username = username
    
    def __repr__(self):
        return "mwclient Wiiki object:\nLogged in as {}.".format(self.username)
    
    def article(self, title):
        if title == "List of Custom Tracks":
            return ListCustomTracks(self.wiiki)
        elif title == "List of Retro Tracks from Non-Mario Kart Games":
            return ListRetrosOtherGames(self.wiiki)
        else:
            return Article(title, self.wiiki)
    
    def search(self, query, where = "title", namespace = 0):
        l = []
        for article in self.wiiki.search(query, namespace, where):
            l.append(article.get("title"))
        if not bool(l):
            return None
        elif len(l) == 1:
            return l[0]
        else:
            return l
    
    def approximate_title(self, title):
        result = self.search(title)
        if result == None:
            return None
        elif type(result) == str:
            return result
        else:
            length = float("inf")
            for article in result:
                if title not in article:
                    continue
                if len(article) < length:
                    approximation = article
                    length = len(approximation)
            return approximation
    
    def text(self, title):
        page = Article(title, self.wiiki)
        return page.text
    
    def edit(self, title, text, summary = "", minor = False):
        page = Article(title, self.wiiki)
        page.object.edit(text, summary, minor)
    
    def move(self, title, new_title, summary = "", redirect = False):
        page = Article(title, self.wiiki)
        page.object.move(new_title, reason = summary, no_redirect = not redirect)
    
    def articles_in_category(self, name):
        category = self.wiiki.categories[name]
        names = set()
        for article in category:
            names.add(article.name)
        return names
    
    def categories_of_article(self, name):
        article = Article(name, self.wiiki)
        categories = set()
        for category in article.object.categories():
            categories.add(category.name)
        return categories
