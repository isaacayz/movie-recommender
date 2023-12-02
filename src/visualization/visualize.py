import pandas as pd
#import matplotlib.pyplot as plt
from src.features.build_features import DataPipeline

columns = ['userid', 'rating', 'title', 'genre', 'timestamp']
condition = 'r.movieid = m.movieid'
rating = "ratings"
movie = "movies"

class VisualPipeline:
    def __init__(self, moviesToDf) -> None:
        self.data = moviesToDf

    def getMean():
        data = DataPipeline(
            final=[],
            columns= columns,
            rating=rating
        )

        df = DataPipeline.covertMoviesToDf()

        max_rating = df.groupby('userid').mean()
        print(max_rating)