# -*- coding: utf-8 -*-
"""Copy of Multiple Linear Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19ydNPYffcMWeRqiQiB17I-upl0rbneEP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from word2number import w2n

df = pd.read_csv("/content/hiring.csv")

df

# DATA PRE-PROCESSING
df['experience'] = df['experience'].fillna('zero') # Fill na values
df.experience = df.experience.apply(w2n.word_to_num) # to convert str to Number
df

model = linear_model.LinearRegression()
model.fit(df[['c']],df.salary)
model.predict([[2,9,6]])

model.coef_

model.intercept_

2812.95487627*2+1845.70596798*9+2205.24017467*6-17737.263464337688 # Using Formula Method

# y = m1x+m2x+m3x-b