from dataclasses import dataclass
from psycopg2 import sql
import pandas as pd
import sys
from src.exceptions import CustomException
from src.data import database


cursor = database.cursor

class DataPipeline:
    def __init__(self, columns : list) -> None:
        self.final = []
        self.columns = columns
        self.rating = 'ratings'

    
    def fetchMovies(self) -> list:
        try:
            select_query = sql.SQL('SELECT userid, rating, title, genre, timestamp FROM {} AS r LEFT JOIN movies AS m on r.movieId = m.movieId LIMIT 1000').format(
                #sql.SQL(',').join(map(sql.Identifier, self.columns)),
                sql.Identifier(self.rating)
            )

            cursor.execute(select_query)
            testData = cursor.fetchall()
            return testData


        except Exception as e:
            raise CustomException(e, sys)


    
    def dateConversion(self, data) -> list:
        """
        Please make sure it's the last column in the list/dataset
        """
        for date in data:
            conv = list(date)
            temp = conv[-1].strftime("%Y-%m-%d %H:%M:%S")
            conv[-1] = temp
            self.final.append(conv)
        
        #print(self.final)    
        return self.final
    

    def dateTimeExtraction(self, data) -> pd.DataFrame:
        """
        Converts the passed date in a dataframe to different columns of date and time
        """
        data['Date'] = data['Timestamp'].apply(lambda x : x.split()[0])
        data['Time'] = data['Timestamp'].apply(lambda x : x.split()[1])

        return data

    
    def covertMoviesToDf(self, data) -> pd.DataFrame:
        df = pd.DataFrame(data, index=None, columns=self.columns)
        return df
    

    def fetchMoviesDetails(self) -> list:
        try:
            select_query = sql.SQL('SELECT year, r.userid, rating, tag, relevance, r.timestamp FROM {} AS m JOIN ratings AS r ON m.movieId = r.movieId JOIN genome_scores AS gs ON gs.movieId = gs.movieId JOIN tags as t ON r.userId = t.userId LIMIT 10').format(
                #sql.SQL(',').join(map(sql.Identifier, c)),
                sql.Identifier('movies')
            )
            cursor.execute(select_query)
            data = cursor.fetchall()

        except Exception as e:
            raise CustomException(e, sys)
        
        return data
    