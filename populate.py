#!/usr/bin/python

import sqlite3

print
print "Run only once or you will get error for duplicates"
print 

conn = sqlite3.connect('picture_share.db')
c = conn.cursor()

# Add one user
user=('dave@gmail.com', 'dave123', 'NULL', 'NULL', 'NULL', 'NULL')
c.execute('INSERT INTO users VALUES (?,?,?,?,?,?)', user)

# Larger example that inserts many records at a time
users = [('george@gmail.com', 'abc123', 'NULL', 'NULL', 'NULL', 'NULL'),
             ('mary@gmail.com', 'mary123', 'NULL', 'NULL', 'NULL', 'NULL'),
             ('peter@gmail.com', 'peter123', 'NULL', 'NULL', 'NULL', 'NULL'),
             ('frank@gmail.com', 'frank123', 'NULL', 'NULL', 'NULL', 'NULL'),
             ('susan@gmail.com', 'susan123', 'NULL', 'NULL', 'NULL', 'NULL'),
             ('edward@gmail.com', 'edward123', 'NULL', 'NULL', 'NULL', 'NULL'),
             ('betty@gmail.com', 'betty123', 'NULL', 'NULL', 'NULL', 'NULL'),
            ]
c.executemany('INSERT INTO users VALUES (?,?,?,?,?,?)', users)

albums = [("album1",'george@gmail.com',"public"),
           ("album2",'george@gmail.com',"public"),
           ("album3",'george@gmail.com',"private"),
           ("album1",'mary@gmail.com',"public"),
         ]
c.executemany('INSERT INTO albums VALUES (?,?,?)', albums)

pictures = [
             ("image-89.jpg","album1","george@gmail.com"),
             ("image-90.jpg","album1","george@gmail.com"),
             ("image-91.jpg","album1","george@gmail.com"),
             ("image-92.jpg","album1","george@gmail.com"),
             ("image-93.jpg","album1","george@gmail.com"),
             ("image-94.jpg","album1","george@gmail.com"),
             ("image-95.jpg","album1","george@gmail.com"),
             ("image-96.jpg","album1","george@gmail.com"),
             ("image-97.jpg","album1","george@gmail.com"),
             ("image-98.jpg","album1","george@gmail.com"),
             ("image-99.jpg","album1","george@gmail.com"),
             ("image-100.jpg","album1","george@gmail.com"),
             ("image-101.jpg","album1","george@gmail.com"),
             ("image-102.jpg","album1","george@gmail.com"),
             ("image-103.jpg","album1","george@gmail.com"),
             ("image-104.jpg","album1","george@gmail.com"),
             ("image-105.jpg","album1","george@gmail.com"),
             ("image-106.jpg","album1","george@gmail.com"),
             ("image-107.jpg","album1","george@gmail.com"),
             ("image-108.jpg","album1","george@gmail.com"),
             ("image-109.jpg","album1","george@gmail.com"),
             ("image-110.jpg","album1","george@gmail.com"),
           ]

c.executemany('INSERT INTO pictures VALUES (?,?,?)', pictures)

circles = [
            ('george@gmail.com', 'Buddies'),
            ('george@gmail.com', 'Family'),
            ('george@gmail.com', 'Coworkers'),
            ('george@gmail.com', 'School'),
            ('george@gmail.com', 'Others'),
          ]
c.executemany('INSERT INTO circles VALUES (?,?)', circles)
          
friendlist = [
               ("george@gmail.com", "mary@gmail.com", "NULL"),
               ("george@gmail.com", "peter@gmail.com", "NULL"),
               ("george@gmail.com", "frank@gmail.com", "NULL"),
               ("george@gmail.com", "susan@gmail.com", "NULL"),
               ("george@gmail.com", "edward@gmail.com", "NULL"),
               ("george@gmail.com", "betty@gmail.com", "NULL"),
             ]
c.executemany('INSERT INTO friendlist VALUES (?,?,?)', friendlist)
               
# commit or there are no changes
conn.commit()

print 'Done.'