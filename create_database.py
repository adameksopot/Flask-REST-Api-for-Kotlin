import sqlite3

connection = sqlite3.connect('db.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS location (id integer primary key autoincrement,latitude real,longitude real)"
cursor.execute(create_table)
connection.commit()
connection.close()