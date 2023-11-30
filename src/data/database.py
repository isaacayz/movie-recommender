import psycopg2
import constants as constants


password = constants.password
database = constants.db_name

class TestDb():
    pass

db_params = {
    'database': database,
    'user': 'postgres',
    'password': password,
    'host' : 'localhost',
    'port' : '5432'
}


conn = psycopg2.connect(**db_params)
cursor = conn.cursor()


def closeConnection():
    conn.commit()
    cursor.close()
    conn.close()
    print("DB connection closed successfully!")
