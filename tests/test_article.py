def test_can_create_article():
    author = Author("Test Writer")
    author.save()
    magazine = Magazine("Tech Today", "Technology")
    magazine.save()
    article = Article("AI is Here", author.id, magazine.id)
    article.save()
    assert article.id is not None

def test_article_links_to_author_and_magazine():
    article = Article.find_by_title("AI is Here")
    assert article.author().name == "Test Writer"
    assert article.magazine().name == "Tech Today"
