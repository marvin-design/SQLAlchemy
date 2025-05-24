def test_magazine_articles_and_contributors():
    magazine = Magazine.find_by_name("Tech Today")
    articles = magazine.articles()
    contributors = magazine.contributors()
    assert len(articles) > 0
    assert len(contributors) > 0

def test_contributing_authors_filter():
    magazine = Magazine.find_by_name("Tech Today")
    top_authors = magazine.contributing_authors()
    for author in top_authors:
        assert len(author.articles()) > 2
