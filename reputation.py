import mysql.connector

with open('db.pwd') as f:
    pwd = f.readlines()[0]

cnx = mysql.connector.connect(user='root', password = pwd, host = '127.0.0.1', database = 'Netflix')
cursor = cnx.cursor()

for i in range(15):
    query = 'insert into s(select movie_id, avg(rating*users.reputation) as score from ratings, users where users.id=ratings.user_id and movie_id>='+str(i*1000)+' and movie_id<'+str((i+1)*1000)+' group by movie_id)'
    cursor.execute(query)
    cnx.commit()
    print i

cursor.close()
cnx.close()
