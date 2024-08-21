import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns

#import CSV file and create dataframe
df = pd.read_csv('/Users/victordecolvenaer/Documents/python_scripts/diabetes_data/diabetes.csv')

#remove rows with missing values or only zeroes
df.loc[(df!=0).any(axis=1)]
df.dropna()

