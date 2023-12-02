from src.features.build_features import DataPipeline
from src.data import database as db
from src.visualization.visualize import VisualPipeline
import time


columns = ['userid', 'rating', 'title', 'genre', 'timestamp']
condition = 'r.movieid = m.movieid'
rating = "ratings"
movie = "movies"

def getMean():
    data = DataPipeline(
            final=[],
            columns= columns,
            rating=rating
            )

    df = data.covertMoviesToDf(data.convertToDate(data.fetchMovies()))
    finalAnswer = df[['rating', 'userid']].groupby('userid').mean()

    return finalAnswer



#df = data.covertMoviesToDf(data.convertToDate(data.fetchMovies()))


if __name__ == '__main__':
    #print(df[['rating', 'userid']].groupby('userid',).mean())
    print(getMean())
    db.closeConnection()
