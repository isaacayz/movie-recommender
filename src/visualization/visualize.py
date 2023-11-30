import pandas as pd
#import matplotlib.pyplot as plt
from src.features.build_features import DataPipeline

df = DataPipeline.covertMoviesToDf()

max_rating = df.groupby('userid').mean()
print(max_rating)