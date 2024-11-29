from openpyxl import Workbook, load_workbook
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, accuracy_score
from keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import cross_val_score
from scikeras.wrappers import KerasClassifier, KerasRegressor
import warnings
warnings.filterwarnings("ignore")

from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Input, Dropout
import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns

def plot_confusion_matrix(y_test, y_predict, name):
    cm = confusion_matrix(y_test, y_predict)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predichos')
    plt.ylabel('Verdaderos')
    plt.title('Matriz de Confusión')
    plt.savefig(name)
    plt.show()
    return None

def get_metrics(y_test, y_predict, name):
    precision = precision_score(y_test, y_predict, average=None, zero_division=0)
    recall = recall_score(y_test, y_predict, average=None, zero_division=0)
    f1 = f1_score(y_test, y_predict, average=None, zero_division=0)
    accuracy = accuracy_score(y_test, y_predict)
    encabezado = ['Clase']
    Precision = ['Precision']
    Recall = ['Recall']
    F1_Score = ['F1-Score']
    Accuracy = ['Accuracy', accuracy]
    labels = {0: 'Healthy', 1: 'No Healthy'}
    for i in range(len(precision)):
        encabezado.append(labels[i])
        Precision.append(precision[i])
        Recall.append(recall[i])
        F1_Score.append(f1[i])
    Salida = [Accuracy, encabezado, Precision, Recall, F1_Score]
    Dataframe = pd.DataFrame(Salida)
    export_data_xlsx(Dataframe, name)
    return None

def export_data_xlsx(Dataframe, name):
    file_path = 'metrics.xlsx'
    if not os.path.exists(file_path):
        metrics_file = Workbook()
        metrics_file.save(file_path)
    with pd.ExcelWriter(file_path, mode="a", engine='openpyxl', if_sheet_exists='replace') as writer:
        Dataframe.to_excel(writer, sheet_name=name)
    return None

def plot_data_NN(data):
    plt.subplot(1,2,1)
    plt.plot(data.history['accuracy'], '-')
    plt.plot(data.history['val_accuracy'], '-')
    plt.title('Precisión del modelo')
    plt.ylabel('Precisión')
    plt.xlabel('Época')
    plt.legend(['Entrenamiento', 'Validación'], loc='upper left')
    plt.subplot(1,2,2)
    plt.plot(data.history['loss'], '-')
    plt.plot(data.history['val_loss'], '-')
    plt.title('Pérdida del modelo')
    plt.ylabel('Pérdida')
    plt.xlabel('Época')
    plt.legend(['Entrenamiento', 'Validación'], loc='upper left')
    plt.show()
    return None