class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
            
    @property 
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if(hasattr(self, "title")):
            print("Already Exists")
        else:
            if isinstance(title, str) and 5 <= len(title) <= 50:
                self._title = title

    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self,magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine




class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if(hasattr(self, "name")):
            print("Already Exists")
        else:
             if isinstance(name, str) and len(name) > 0:
                  self._name = name
                  

    
    def articles(self):
        return [article for article in Article.all if article.author == self]
    
    
    
    def magazines(self):
        magazines = [article.magazine for article in Article.all if article.author == self]
        unique_values = set(magazines)
        return list(unique_values)

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        topics = list(set(article.magazine.category for article in Article.all if article.author == self))
        return topics if topics else None

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category

    def articles(self):
        magazines = [article for article in Article.all if article.magazine == self]
        unique_values = set(magazines)
        return list(unique_values)

    def contributors(self):
         magazines = list(set(article.author for article in Article.all if article.magazine == self))
         return magazines

    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self]
        return titles if titles else None

    def contributing_authors(self):
        authors = [article.author for article in Article.all if article.magazine == self]
        author_count = {author: authors.count(author) for author in set(authors)}
        contributing_authors = [author for author, count in author_count.items() if count > 2]
        return contributing_authors if contributing_authors else None
        
        
            
   
    
   