# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BE8oN7eFquoFvAR-2OOfCd7etjrI1ZJ0
"""



import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("titanic.csv")
df.head()
df["Survived"].plot

