import sqlite3

with open("main.sql", "r") as file:
  sql_script = file.read()
  sqlite3.connect("school.db").executescript(sql_script)