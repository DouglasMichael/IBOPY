from PyQt5.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import mplcursors  # Importe a biblioteca mplcursors
plt.style.use('bmh')

    
class analizarDados(QWidget):
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)
        
    def plot_tree_predictions(self, acao):
        # Coloque o código de plotagem aqui
        future_days = 25
        df = pd.read_csv("C:/Users/Pichau/Desktop/IBOPY/acoes/" + acao + ".csv")
        df['Prediction'] = df['Close'].shift(-future_days)
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.dropna()
        X = np.array(df.drop(['Prediction', 'Date'], axis=1))[:-future_days]
        Y = np.array(df['Prediction'])[:-future_days]
        x_train, x_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)
        tree = DecisionTreeRegressor()
        tree.fit(x_train, Y_train)
        x_future = np.array(df.drop(['Prediction', 'Date'], axis=1).tail(future_days))
        tree_prediction = tree.predict(x_future)
        last_year_data = df[df['Date'] > df['Date'].max() - pd.DateOffset(years=1)]
        Predictions = tree_prediction
        valid = df[X.shape[0]:]
        valid['Predictions'] = Predictions

        self.canvas.axes.clear()
        self.canvas.axes.plot(last_year_data['Date'], last_year_data['Close'], label='Original - Último Ano')
        self.canvas.axes.plot(valid['Date'], valid[['Close', 'Predictions']])
        self.canvas.axes.legend(['Original', 'Validação', 'Predição'])
        self.canvas.axes.set_title('Modelo de Árvore de Decisão - Último Ano')
        self.canvas.axes.set_xlabel('Data')
        self.canvas.axes.set_ylabel('Preço de Fechamento em USD ($)')

        # Adicionar a funcionalidade do mplcursors
        mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(f"{sel.artist.get_label()}: {sel.target[1]:.2f}"))

        self.canvas.draw()