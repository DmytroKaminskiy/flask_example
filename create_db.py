import sqlite3

conn = sqlite3.connect('users.db')
cur = conn.cursor()

# Create table
cur.execute('''
CREATE TABLE emails
(UserName varchar(255), Email varchar(128) UNIQUE)
''')

# user_name, email

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
