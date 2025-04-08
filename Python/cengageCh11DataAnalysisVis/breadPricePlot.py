import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

frame = pd.read_csv("breadprice.csv")

frame.fillna(0, inplace=True)
#print(frame)

frame.drop(columns = "Year", inplace=True)
#print(frame)

#averageList = []

#for row in range(len(frame)):
#    averageList.append(frame.loc[row].mean())
#print(averageList)

frame.loc[0:9].plot(marker='o')
plt.title('Price of Bread')
plt.xlabel('Years 2012 - 2022')
plt.ylabel('Bread Price')
plt.show()