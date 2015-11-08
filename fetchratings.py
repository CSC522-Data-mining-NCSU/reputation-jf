import mysql.connector
import pickle

with open('db.pwd') as f:
    pwd = f.readlines()[0]

cnx = mysql.connector.connect(user='root', password = pwd, host = '127.0.0.1', database = 'Netflix')
cursor = cnx.cursor()

###############################################
# calcualting the ground truth for each movie #
###############################################
query = 'select user_id,rating,movie_id from ratings'
cursor.execute(query)
result = open('raw_rating','wb')

m = [[x[0],float(x[1]),x[2]] for x in cursor]
pickle.dump(m,result)

cursor.close()
cnx.close()
result.close()
