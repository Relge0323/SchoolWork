import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

frame = pd.read_csv("breadprice.csv")

frame.fillna(0, inplace=True)
print(frame)

frame.drop(columns = "Year", inplace=True)
print(frame)

averageList = []

for row in range(len(frame)):
    averageList.append(frame.loc[row].mean())
print(averageList)