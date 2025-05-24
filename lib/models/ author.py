from lib.db.connection import get_connection

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def create(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?) RETURNING id", (name,))
        id = cursor.fetchone()["id"]
        conn.commit()
        conn.close()
        return cls(id=id, name=name)

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(id=row["id"], name=row["name"])
        return None

    def articles(self):
        from lib.models.article import Article
        return Article.find_by_author_id(self.id)

    def magazines(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.* FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        conn.close()
        from lib.models.magazine import Magazine
        return [Magazine(row["id"], row["name"], row["category"]) for row in rows]

    def add_article(self, magazine, title):
        from lib.models.article import Article
        return Article.create(title=title, author_id=self.id, magazine_id=magazine.id)

    def topic_areas(self):
        return list({m.category for m in self.magazines()})
