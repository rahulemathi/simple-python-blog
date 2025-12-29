#create a database using sqlite3

#import sqlite3

#conn = sqlite3.connect('dbname.db')

#cursor = conn.cursor()

#write the query to create a table

#conn.commit()

#conn.close()

import sqlite3

conn = sqlite3.connect('blog.db')

cursor = conn.cursor()

# Create users table

cursor.execute(''' CREATE TABLE IF NOT EXISTS blogs(
               id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               title TEXT,
               image TEXT,
               description TEXT,
               author TEXT,
               date TEXT
               )  ''')

cursor.execute(''' CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               username TEXT,
               email TEXT,
               password BLOB
               )  ''')

cursor.execute(''' CREATE TABLE IF NOT EXISTS comments(
               id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
              blog_id INTEGER,
               comment TEXT,
               user_id INTEGER
               )  ''')

cursor.execute(''' ALTER TABLE blogs ADD COLUMN user_id INTEGER ''')

# cursor.execute(''' INSERT INTO blogs(title, image, description) 
#                 VALUES(?,?,?) ''' ,
#                ('demo','NULL','demo data etc'))
conn.commit()

conn.close()