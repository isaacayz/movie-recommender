import psycopg2

db_params = {
    'database': 'movie_db',
    'user': 'postgres',
    'password': 'P@$$w0rd',
    'host' : 'localhost',
    'port' : '5432'
}


conn = psycopg2.connect(**db_params)
cursor = conn.cursor()


def closeConnection():
    cursor.close()
    conn.close()
