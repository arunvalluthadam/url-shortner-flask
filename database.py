import sqlite3

conn = sqlite3.connect("smallurl.db")
cur = conn.cursor()
cur.execute("CREATE TABLE if not EXISTS urlshort (longurl string, shorturl TEXT)")
conn.commit()

