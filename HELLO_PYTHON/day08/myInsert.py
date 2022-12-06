import psycopg2

connection = psycopg2.connect(database="python", user="postgres", password="python")
cur = connection.cursor()

sql = """
    insert into sample
        (col01,col02,col03)
    values
        ('3','3','3')
"""

cur.execute("insert into sample (col01,col02,col03) values('3','3','3')")

print("cnt",cur.rowcount)

connection.commit()
cur.close()
connection.close()