import pandas as pd
import numpy as np

my_series = [5,9,12,27]
my_var = pd.Series(my_series)



my_index = ["a", "b", "c", "d"]
my_var2 = pd.Series(my_series, my_index)





cars = {"Tesla": 12, "Mercedes":42, "BMW":3}
my_var3 = pd.Series(cars)
print(my_var3)


print(my_var3["Tesla"])