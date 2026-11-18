import sqlite3

conn = sqlite3.connect(
    "autofounder.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS projects(

id INTEGER PRIMARY KEY,

business TEXT,

report TEXT
)
""")

conn.commit()


def save_project(
        business,
        report
):

    cursor.execute(
        """
        INSERT INTO projects
        (business,report)
        VALUES(?,?)
        """,
        (business,report)
    )

    conn.commit()

def get_projects():

    cursor.execute(
        "SELECT * FROM projects"
    )

    return cursor.fetchall()