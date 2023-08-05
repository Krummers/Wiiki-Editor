import mwclient as mc

from .article import Article
from .lists.listcustomtracks import ListCustomTracks, Table, Entry

class Wiiki(object):
    
    def __init__(self, username, password, api):
        wiiki = mc.Site("wiki.tockdom.com", clients_useragent = api)
        wiiki.login(username, password)
        self.wiiki = wiiki
        self.username = username
    
    def __repr__(self):
        return "mwclient Wiiki object:\nLogged in as {}.".format(self.username)
    
    def article(self, title):
        if title == "List of Custom Tracks":
            return ListCustomTracks(self.wiiki)
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
    
    def edit(self, title, text, summary = ""):
        page = Article(title, self.wiiki)
        page.object.edit(text, summary)
    
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

class HTMLSort(object):
    
    def __init__(self, string):
        txt = open("Sort.txt", "r", encoding = "utf-8")
        characters = txt.readlines()
        txt.close()
        for x in range(len(characters)):
            characters[x] = characters[x][0]
        
        self.letters = []
        self.orders = []
        
        for letter in string.lower():
            self.letters.append(letter)
            self.orders.append(characters.index(letter))
    
    def __str__(self):
        return "".join(self.letters)
    
    def __repr__(self):
        return str(self)
    
    def __lt__(self, other):
        if type(other) != HTMLSort:
            raise TypeError("only objects of type 'Sort' are supported")
        for x in range(min(len(self), len(other))):
            if self.orders[x] < other.orders[x]:
                return True
        if len(self) < len(other):
            return True
        return False
    
    def __le__(self, other):
        if type(other) != HTMLSort:
            raise TypeError("only objects of type 'Sort' are supported")
        return self == other or self < other
    
    def __eq__(self, other):
        if type(other) != HTMLSort:
            raise TypeError("only objects of type 'Sort' are supported")
        if self.orders == other.orders:
            return True
        else:
            return False
    
    def __gt__(self, other):
        if type(other) != HTMLSort:
            raise TypeError("only objects of type 'Sort' are supported")
        for x in range(min(len(self), len(other))):
            if self.orders[x] < other.orders[x]:
                return False
        if len(self) < len(other):
            return False
        return True
    
    def __ge__(self, other):
        if type(other) != HTMLSort:
            raise TypeError("only objects of type 'Sort' are supported")
        return self == other or self > other
    
    def __ne__(self, other):
        if type(other) != HTMLSort:
            raise TypeError("only objects of type 'Sort' are supported")
        if self.orders != other.orders:
            return True
        else:
            return False
    
    def __len__(self):
        return len(self.letters)
