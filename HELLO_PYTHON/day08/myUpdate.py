import psycopg2

col01 = '4'
col02 = '7'
col03 = '7'

connection = psycopg2.connect(database="python", user="postgres", password="python")
cur = connection.cursor()

sql = f"""
    update sample 
    set 
        col02='{col02}', col03='{col03}'
    where 
        col01='{col01}'
"""

cur.execute(sql)

print("cnt",cur.rowcount)

connection.commit()
cur.close()
connection.close()