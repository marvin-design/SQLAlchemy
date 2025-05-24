from lib.db.connection import get_connection

class Magazine:
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?) RETURNING id", (self.name, self.category))
        self.id = cursor.fetchone()[0]
        conn.commit()
        conn.close()

    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        return cursor.fetchall()

    def contributors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT DISTINCT a.* FROM authors a
        JOIN articles ar ON ar.author_id = a.id
        WHERE ar.magazine_id = ?
        """, (self.id,))
        return cursor.fetchall()

    def contributing_authors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT a.* FROM authors a
        JOIN articles ar ON ar.author_id = a.id
        WHERE ar.magazine_id = ?
        GROUP BY a.id
        HAVING COUNT(ar.id) > 2
        """, (self.id,))
        return cursor.fetchall()
