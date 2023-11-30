from psycopg2 import sql
import pandas as pd
import sys
from src.exceptions import CustomException
from src.data import database


cursor = database.cursor

class DataPipeline:
    def __init__(self, final: list, columns: list, rating: str) -> None:
        self.final = final
        self.columns = columns
        self.rating = rating

    def fetchMovies(self):
        try:
            select_query = sql.SQL('SELECT {} FROM {} AS r LEFT JOIN movies AS m on r.movieId = m.movieId LIMIT 1000').format(
                sql.SQL(',').join(map(sql.Identifier, self.columns)),
                sql.Identifier(self.rating)
            )

            cursor.execute(select_query)
            testData = cursor.fetchall()
            return testData


        except Exception as e:
            raise CustomException(e, sys)



    def convertToDate(self, data):
        for date in data:
            conv = list(date)
            temp = conv[-1].strftime("%Y-%m-%d %H:%M:%S")
            conv[-1] = temp
            self.final.append(conv)
        
        #print(self.final)    
        return self.final


    def covertMoviesToDf(self, data):
        df = pd.DataFrame(data, index=None, columns=self.columns)
        #print(df)
        return df
    