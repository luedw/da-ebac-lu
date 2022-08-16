import csv

with open('gasolina.csv') as file:
  line_reader = csv.reader(file)

import pandas as pd
import matplotlib.pyplot as plt

gasolina = pd.read_csv('gasolina.csv',sep=',')