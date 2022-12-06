import psycopg2

connection = psycopg2.connect(database="python", user="postgres", password="python")
cursor = connection.cursor()

cursor.execute("select col01,col02,col03 from sample")
rows=cursor.fetchall() 

for i in rows:
    print(i)

cursor.close()
connection.close()