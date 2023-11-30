from src.features.build_features import DataPipeline
from src.data import database as db


columns = ['userid', 'rating', 'title', 'genre', 'timestamp']
condition = 'r.movieid = m.movieid'
rating = "ratings"
movie = "movies"

data = DataPipeline(
    final=[],
    columns= columns,
    rating=rating
)



if __name__ == '__main__':
    #tempMovies = data.fetchMovies()
    #data.convertToDate(tempMovies)
    data.covertMoviesToDf(data.convertToDate(data.fetchMovies()))
    db.closeConnection()
