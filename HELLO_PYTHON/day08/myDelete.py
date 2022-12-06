import psycopg2

col01 = '4'

connection = psycopg2.connect(database="python", user="postgres", password="python")
cur = connection.cursor()

sql = f"""
    delete from sample 
    where 
        col01='{col01}'
"""

cur.execute(sql)

print("cnt",cur.rowcount)

connection.commit()
cur.close()
connection.close()