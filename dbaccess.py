import mysql.connector

with open('db.pwd') as f:
    pwd = f.readlines()[0]

cnx = mysql.connector.connect(user='root', password = pwd, host = '127.0.0.1', database = 'Netflix')
cursor = cnx.cursor()
cursor2 = cnx.cursor()

###############################################
# calcualting the ground truth for each movie #
###############################################
query = 'select rating,movie_id from ratings where movie_id > 15074'
cursor.execute(query)
result = open('movie_ground.txt','w')

movie_pointer = 1
movie_count = 0
sum = 0

for x in cursor:
    if x[1] == movie_pointer:
        movie_count += 1
        sum += x[0]
    else:
        result.write(str(movie_pointer)+ ' ' +str(round(sum/movie_count,3))+'\n')
        movie_pointer = x[1]
        movie_count = 0
        sum = 0
        if movie_pointer % 100 == 0: print movie_pointer
"""
 update_sql = 'update movies set ground_rating = '+str(round(sum/movie_count,3))+' where id = '+str(movie_pointer)
 cursor2.execute(update_sql)
"""

cursor.close()
#cursor2.close()
cnx.close()
result.close()
