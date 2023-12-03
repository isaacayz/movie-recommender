from src.features.build_features import DataPipeline
from src.data import database as db
from src.visualization.visualize import VisualPipeline
import time



columns = ['userid', 'rating', 'title', 'genre', 'timestamp']
movieColumns = ['ReleasedYear', 'UserRated', 'Rating', 'Tag', 'GS_Relevance', 'Timestamp']
movieData = DataPipeline(columns=movieColumns)

def getMean():
    data = DataPipeline(
            columns= columns,
            )

    df = data.covertMoviesToDf(data.dateConversion(data.fetchMovies()))
    finalAnswer = df[['rating', 'userid']].groupby('userid').mean()

    return finalAnswer


data =  movieData.dateTimeExtraction(movieData.covertMoviesToDf(movieData.dateConversion(movieData.fetchMoviesDetails())))
#df = data.covertMoviesToDf(data.convertToDate(data.fetchMovies()))


if __name__ == '__main__':
    #print(df[['rating', 'userid']].groupby('userid',).mean())
    print(data)
    db.closeConnection()
