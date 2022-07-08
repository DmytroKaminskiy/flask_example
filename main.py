from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route('/emails/create/')
def email_create():
    email = request.args['email']
    name = request.args['name']

    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        INSERT INTO emails
        VALUES ('{name}', '{email}');
        '''
        cur.execute(sql)
        conn.commit()
    finally:
        conn.close()

    return 'Emails Create'


@app.route('/emails/read/')
def email_read():
    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        SELECT * FROM emails;
        '''
        cur.execute(sql)
        emails = cur.fetchall()

    finally:
        conn.close()

    return str(emails)



@app.route('/emails/delete/')
def email_delete():
    email = request.args['email']
    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        DELETE FROM emails WHERE Email == '{email}';
        '''
        cur.execute(sql)
        conn.commit()
    finally:
        conn.close()

    return 'Emails Delete'



@app.route('/emails/update/')
def email_update():
    email = request.args['email']
    name = request.args['name']

    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        UPDATE emails
        SET UserName = '{name}'
        WHERE Email == '{email}';
        '''
        cur.execute(sql)
        conn.commit()
    finally:
        conn.close()

    return 'Emails Update'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

'''
http:// 172.27.201.140 :5000 / ?length=20&name=Dima&age=30
1       2                 3  4  5

1. protocol
   http:// https:// ftp:// (filezilla) smtp:// amqp://

2. Destination. Domain, IPv4, IPv6
IPv4
0-255.0-255.0-255.0-255
0.0.0.0 - yes
254.0.0.1 - yes
254.0.0.0.1 - no
254.0.1 - no

localhost - 127.0.0.1

3. Port - 0 - 65_535
0 - root
80 - http
443 - https

4 Path

5 Query string


Stateless
Stateful

==
!=
>
>=
<
<=


NOT
AND
OR

CRUD
C - Create
R - Read
U - Update
D - Delete

'''
