import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns

#import CSV file and create dataframe
df = pd.read_csv('/Users/victordecolvenaer/Documents/python_scripts/netflix_data/netflix.csv')

#Exploratory Data Analysis to have insight in dataset
column_names = str(df.columns)
tabel_format = str(df.shape)
summary = str(df.describe)
missing_values = str(df.isnull().sum())
data_types = str(df.dtypes)

#print exploratory information in txt file
output = open('output.txt','w')
print("column names\n" + column_names, file = output)
print("tabel format\n" + tabel_format, file = output)
print("summary\n" + summary, file = output)
print("missing value\n" + missing_values, file = output)
print("data types\n" + data_types, file = output)

#print unique values in numerical columns
movie_type = str(df['type'].unique())
release_year = str(df['release_year'].unique())
age_certification = str(df['age_certification'].unique())
runtime = str(sorted(df['runtime'].unique()))
imdb_score = str(sorted(df['imdb_score'].unique()))

print("movie_type\n" + movie_type, file = output)
print("release_year\n" + release_year, file = output)
print("age_certification\n" + age_certification, file = output)
print("runtime\n" + runtime, file = output)
print("imdb_score\n" + imdb_score, file = output)

#create PDF file to save figures from following visualisations
pdf_filename = 'output_plots.pdf'

#create some exploratory data visualisations
numerical_columns = ['release_year','runtime','imdb_score']
categorical_columns = ['type','age_certification']
correlation_matrix = df[numerical_columns].corr()


with PdfPages(pdf_filename) as pdf_pages:
    for col in numerical_columns:
        plt.figure()
        sns.histplot(df[col])
        plt.title(col)
        pdf_pages.savefig()
        plt.close()

    for col in categorical_columns:
        plt.figure()
        sns.countplot(data=df, x=col)
        plt.title(col)
        pdf_pages.savefig()
        plt.close()

    #create scatterplots with imdb_score
    figure, subplot = plt.subplots(2,2)
    x_labels = ['release_year','runtime','imdb_votes','imdb_score']
    for i,data in enumerate(x_labels):
        sns.scatterplot(x=df[data], y=df['imdb_score'],ax = subplot[i//2,i%2])
        subplot[i//2,i%2].set_xlabel({data})
        subplot[i//2,i%2].set_ylabel('IMDB Score')
        subplot[i//2,i%2].set_title(f'Scatterplot of {data} vs IMDB Score')

    pdf_pages.savefig()
    plt.close()

    # Visualize correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    pdf_pages.savefig()
    plt.close()