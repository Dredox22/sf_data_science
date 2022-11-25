import numpy as np
print(np.sctypeDict)
print(len(np.sctypeDict))
# 158, но может быть 135 или 139
import pandas as pd
print(pd.__name__)
print (pd.__version__)

import pandas as pd
countries = pd.Series(
    data = ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
    index = ['UK', 'CA', 'US', 'RU', 'UA', 'BY', 'KZ'],
    name = 'countries'
)
print(countries)