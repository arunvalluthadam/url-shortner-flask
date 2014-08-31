import sqlite3

conn = sqlite3.connect("smallurl.db")
cur = conn.cursor()
cur.execute("CREATE TABLE if not EXISTS urlshort (longurl string primary key, shorturl TEXT)")
conn.commit()

