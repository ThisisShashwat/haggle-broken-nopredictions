"""Deliberately broken: it never writes predictions.csv."""

import pandas as pd

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
guess = train["hours_spent"].mean()
print("my guess is", guess)
