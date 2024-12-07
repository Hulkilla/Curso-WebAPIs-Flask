import sqlite3 as SQL

route_db = "data/dictionary.db"

def match_exact(word: str) -> list:
    """
    This method will:
    1. Accept a string
    2. Search the dictionary for an exact match
    3. If success return the definition
    4. If not return an empty list
    """

    db = SQL.connect(route_db)
    sql_query = "select * from entries where word=?"
    match = db.execute(sql_query, (word,)).fetchall()
    db.commit()
    db.close()

    return match




def match_like(word: str) -> list:
    """
    This method will:
    1. Accept a string
    2. Search the dictionary for approximate matches
    3. If success return the definition as a list
    4. If not return an empty list
    """

    db = SQL.connect(route_db)
    sql_query = "select * from entries where word like ?"
    match = db.execute(sql_query, (f"%{word}%",)).fetchall()
    db.commit()
    db.close()

    return match

