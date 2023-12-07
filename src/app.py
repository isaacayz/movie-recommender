from src.features.build_features import DataPipeline, data
from src.data import database as db
from src.visualization.visualize import VisualPipeline
import time



def getMean():
    data = DataPipeline(
            #columns= columns,
            )
    df = data.covertMoviesToDf(data.dateConversion(data.fetchMovies()))
    finalAnswer = df[['rating', 'userid']].groupby('userid').mean()
    return finalAnswer




if __name__ == '__main__':
    print(data.head())
    db.closeConnection()
