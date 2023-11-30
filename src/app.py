from src.features.build_features import DataPipeline
from src.data import database as db
#from src.visualization import visualize
import time


columns = ['userid', 'rating', 'title', 'genre', 'timestamp']
condition = 'r.movieid = m.movieid'
rating = "ratings"
movie = "movies"

data = DataPipeline(
    final=[],
    columns= columns,
    rating=rating
)

df = data.covertMoviesToDf(data.convertToDate(data.fetchMovies()))


if __name__ == '__main__':
    print(df[['rating', 'userid']].groupby('userid',).mean())
    db.closeConnection()
