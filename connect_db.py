import psycopg2



host = "localhost"
database = 'dress_colors'
user = 'postgres'
password = 'binary**'

conn = psycopg2.connect(host=host, database=database, user=user, password=password)

cursor = conn.cursor()

