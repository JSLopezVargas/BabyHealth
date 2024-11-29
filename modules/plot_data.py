import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def boxploter(dataframe):
    columns_to_plot = ['gestweeks','age','gravidity','parity']
    plt.subplot(2, 2, 1)
    sns.boxplot(x=dataframe[columns_to_plot[0]], y=dataframe['babyhealth'])
    plt.subplot(2, 2, 2)
    sns.boxplot(x=dataframe[columns_to_plot[1]], y=dataframe['babyhealth'])
    plt.subplot(2, 2, 3)
    sns.boxplot(x=dataframe[columns_to_plot[2]], y=dataframe['babyhealth'])
    plt.subplot(2, 2, 4)
    sns.boxplot(x=dataframe[columns_to_plot[3]], y=dataframe['babyhealth'])
    plt.tight_layout()
    plt.show()
    return None

def bar_plot(dataframe):
    columns_to_plot = ['sex', 'diabetes', 'hypertension', 'preeclampsia', 'pyrexia', 'meconium', 'noprogress', 'rectype']
    fig, axs = plt.subplots(2, 4, figsize=(20, 10))
    for i, col in enumerate(columns_to_plot):
        pd.crosstab(dataframe[col], dataframe['babyhealth']).plot(kind='bar', ax=axs[i//4, i%4])
        axs[i//4, i%4].set_xlabel(col)
        axs[i//4, i%4].set_ylabel('Count')
        titulo = col + ' vs babyhealth'
        axs[i//4, i%4].set_title(titulo)
        axs[i//4, i%4].legend(title='babyhealth')
    plt.tight_layout()
    plt.show()
    return None

def correlation_plot(dataframe):
    correlation_matrix = dataframe.corr()
    plt.figure(figsize=(15, 15))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, annot_kws={"size": 6})
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.yticks(fontsize=10)
    plt.title('Matriz de Correlación')
    plt.show()
    return None
