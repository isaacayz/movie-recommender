import sys
import os
from dataclasses import dataclass
import csv
from src.exceptions import CustomException


@dataclass
class ImportFilesConfig:
    getFilePath = os.path.abspath()

class ImportFiles:
    # constructor to get the file path
    def __init__(self, path) -> None:
        self.path = os.path.abspath(path)


    #method to read in the file from the path
    def readFile(self):
        try:
            file = self.path
            with open(file, 'r') as file_obj:
                check_ext = os.path.splitext(file_obj)[1]
                if check_ext == 'csv':
                    reader = csv.reader(file_obj)
                    next(reader)
                    return reader
                else:
                    print("File type not supported yet")
                    return(CustomException(sys))
        
        except Exception as e:
            raise CustomException(e, sys)
        
    
    def importFile(self):
        pass

        
