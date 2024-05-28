class Article:
    def __init__(self, author, magazine, title):
        self.author = author 
        self.magazine = magazine  
        self.title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("author must be an instance of Author")
        if hasattr(self, '_author'):
            self._author.remove_article(self)
        self._author = value
        value.add_article(self)

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("magazine must be an instance of Magazine")
        if hasattr(self, '_magazine'):
            self._magazine.remove_article(self)
        self._magazine = value
        value.add_article(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("title must be a non-empty string")
        self._title = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def __setattr__(self, key, value):
        if hasattr(self, key) and key == "_name":
            raise AttributeError("Cannot modify name after instantiation")
        super().__setattr__(key, value)

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, article):
        if not isinstance(article, Article):
            raise TypeError("Can only add instances of Article")
        self._articles.append(article)

    def remove_article(self, article):
        if article in self._articles:
            self._articles.remove(article)

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    def __init__(self, name, category):
        self.name = name  
        self.category = category  
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be of type str")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be of type str")
        if len(value) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = value

    def articles(self):
        return self._articles

    def add_article(self, article):
        if not isinstance(article, Article):
            raise TypeError("Can only add instances of Article")
        self._articles.append(article)

    def remove_article(self, article):
        if article in self._articles:
            self._articles.remove(article)

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        return list(set(article.author.name for article in self._articles))
