import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models.author import Author
from lib.models.article import Article
from lib.models.magazine import Magazine

def test_can_create_author():
    author = Author("Jane Doe")
    author.save()
    assert author.id is not None

def test_find_author_by_name():
    found = Author.find_by_name("Jane Doe")
    assert found.name == "Jane Doe"

def test_author_articles_and_magazines():
    author = Author.find_by_name("Jane Doe")
    assert len(author.articles()) >= 1
    assert len(author.magazines()) >= 1
