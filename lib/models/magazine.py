from lib.db.connection import get_connection

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    @classmethod
    def create(cls, name, category):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?) RETURNING id", (name, category))
        id = cursor.fetchone()["id"]
        conn.commit()
        conn.close()
        return cls(id, name, category)

    def articles(self):
        from lib.models.article import Article
        return Article.find_by_magazine_id(self.id)

    def contributors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT a.* FROM authors a
            JOIN articles ar ON ar.author_id = a.id
            WHERE ar.magazine_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        conn.close()
        from lib.models.author import Author
        return [Author(row["id"], row["name"]) for row in rows]

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT author_id, COUNT(*) as count FROM articles
            WHERE magazine_id = ?
            GROUP BY author_id
            HAVING count > 2
        """, (self.id,))
        rows = cursor.fetchall()
        conn.close()
        from lib.models.author import Author
        return [Author.find_by_id(row["author_id"]) for row in rows]
