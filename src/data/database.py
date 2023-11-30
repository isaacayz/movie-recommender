import psycopg2
import sys
#sys.path.append('/Users/isaacige/Documents/Code/DS&ML/MovieRecommender/src/constants')
from constants import Constants


password = Constants.password
database = Constants.db_name

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


if __name__ == '__main__':
    closeConnection()