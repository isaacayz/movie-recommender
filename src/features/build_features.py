from psycopg2 import sql
import pandas as pd
import sys
from src.exceptions import CustomException


class DataPipeline:
    def __init__(self, final: list, columns: list) -> None:
        self.final = final
        self.columns = columns

    def fetchItems(self):
        try:
            self.columns = ['userid', 'rating', 'title', 'genre', 'timestamp']
            condition = 'r.movieid = m.movieid'
            rating = "ratings"
            movie = "movies"

            
        except Exception as e:
            raise CustomException(e, sys)



    def convertToDate(self, data):
        for date in data:
            conv = list(date)
            temp = conv[-1].strftime("%Y-%m-%d %H:%M:%S")
            conv[-1] = temp
            self.final.append(conv)
            
        return self.final


    def covertToDf(self, data):
        return pd.DataFrame(data, index=None, columns=columns)