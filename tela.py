# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import *
# from PyQt5.uic import loadUi
# from puxarHistorico import BaixarHistorico
# from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
# from analizardados import analizarDados

# class Main(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)

#         loadUi("tela.ui", self)
#         self.BuscarDados = self.findChild(QPushButton, "pushButton")
#         self.comboBox = self.findChild(QComboBox, "comboBox")
#         self.GerarGrafico = self.findChild(QPushButton, "pushButton_3")
#         self.BuscarDados.clicked.connect(self.adicionarAcoes)
#         self.GerarGrafico.clicked.connect(self.gerarGrafico)
#         self.addToolBar(NavigationToolbar(self.analizarDados.canvas, self))
#         self.show()


#     def adicionarAcoes(self):
#         self.BuscarDados.setDisabled(True)
#         acoes = BaixarHistorico()

#         for acao in acoes:
#             self.comboBox.addItem(acao)
    
#     def gerarGrafico(self):
#         print(self.comboBox.currentText())

# if __name__ == '__main__':
#     app = QtWidgets.QApplication([])
#     main = Main()
#     app.exec_()

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QComboBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from puxarHistorico import BaixarHistorico
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from analizardados import analizarDados

class MinhaJanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # Carrega o arquivo de interface do usuário (UI)
        loadUi("tela.ui", self)

        # Encontra o widget criado no arquivo de interface
        self.BuscarDados = self.findChild(QPushButton, "pushButton")
        self.GerarGrafico = self.findChild(QPushButton, "pushButton_3")
        self.comboBox = self.findChild(QComboBox, "comboBox")
        self.widget = self.findChild(QWidget, "analizarDados")
        self.BuscarDados.clicked.connect(self.adicionarAcoes)
        self.GerarGrafico.clicked.connect(self.gerarGrafico)

        # Cria uma instância da classe analizarDados
        self.analizar_dados = analizarDados()
        self.addToolBar(NavigationToolbar(self.analizar_dados.canvas, self))

        # Define o layout para o widget
        layout = QVBoxLayout(self.widget)
        layout.addWidget(self.analizar_dados)

    def adicionarAcoes(self):
        self.BuscarDados.setDisabled(True)
        acoes = BaixarHistorico()

        for acao in acoes:
            self.comboBox.addItem(acao)

    def gerarGrafico(self):
        self.analizar_dados.plot_tree_predictions(acao=self.comboBox.currentText())
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela_principal = MinhaJanelaPrincipal()
    janela_principal.show()
    sys.exit(app.exec_())

