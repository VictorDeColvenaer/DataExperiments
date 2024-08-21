import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns

#import CSV file and create dataframe
df = pd.read_csv('/Users/victordecolvenaer/Documents/python_scripts/diabetes_data/diabetes.csv')

#Exploratory Data Analysis to have insight in dataset
column_names = str(df.columns)
tabel_format = str(df.shape)
summary = str(df.describe)
missing_values = str(df.isnull().sum())
data_types = str(df.dtypes)
info = str(df.info())
zero_values = str((df == 0).sum(axis=0))

#print exploratory information in txt file
output = open('output.txt','w')
print("column names\n" + column_names, file = output)
print("tabel format\n" + tabel_format, file = output)
print("summary\n" + summary, file = output)
print("missing value\n" + missing_values, file = output)
print("data types\n" + data_types, file = output)
print("info\n" + info, file = output)
print("zerovalues in column\n" + zero_values, file = output)


#create PDF file to save figures from following visualisations
pdf_filename = 'output_plots.pdf'

#create some exploratory data visualisations
numerical_columns = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Outcome']
categorical_columns = ['Outcome']
correlation_matrix = df[numerical_columns].corr()


with PdfPages(pdf_filename) as pdf_pages:
    for col in numerical_columns:
        plt.figure()
        sns.boxplot(df[col])
        plt.title(col)
        pdf_pages.savefig()
        plt.close()

    for col in categorical_columns:
        plt.figure()
        sns.countplot(data=df, x=col)
        plt.title(col)
        pdf_pages.savefig()
        plt.close()

    # Visualize correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    pdf_pages.savefig()
    plt.close()

    #visualize pairplot
    plt.figure()
    sns.pairplot(df, hue = "Outcome",kind = 'kde')
    plt.title('pairplot')
    pdf_pages.savefig()
    plt.close()