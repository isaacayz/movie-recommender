import sys
import os
from dataclasses import dataclass
import csv
from src.exceptions import CustomException
import database
import pandas as pd

cursor = database.cursor
table_name = 'links'


@dataclass
class ImportFilesConfig:
    #getFilePath = os.path.abspath()
    pass

class ImportFiles:
    # constructor to get the file path
    def __init__(self, path) -> None:
        self.path = os.path.abspath(path)


    #method to read in the file from the path
    def readFile(self):
        try:
            file = self.path
            with open(file, 'r') as file_obj:
                reader = csv.reader(file_obj)
                next(reader)
                columns = pd.DataFrame(reader, columns=['movieId', 'imdbId', 'tmdbId'])
                col = columns.columns.values
                #iter(reader)
                for row in reader:
                    for c in col:
                        cursor.execute(
                        f"INSERT INTO {table_name} ({col[c]}) VALUES (%s, %s, %s)", 
                        (row[c])
                    )
                return reader, col
        except Exception as e:
            raise CustomException(e, sys)
        
    
    def importFile(self,**cols):
        reader, col = self.readFile()
        print(reader)
        #reader1 = with open(self.readFile())
        try:
            for row in reader:
                for c in col:
                    cursor.execute(
                    f"INSERT INTO {table_name} ({col[c]}) VALUES (%s, %s, %s)", 
                    (row[c])
            )
        except Exception as e:
            raise CustomException(e, sys)

        
importer = ImportFiles('/Users/isaacige/Documents/Code/DS&ML/MovieRecommender/data/links.csv')
importer.readFile()

if __name__ == '__main__':
    database.closeConnection()