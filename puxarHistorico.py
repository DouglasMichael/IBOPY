from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import os
import sys

# Obtém o diretório do script em execução
caminho = os.path.dirname(sys.argv[0])
caminho = caminho.replace("/","\\")

def apagarHistorico():
    arquivos = os.listdir(caminho+"\\acoes")

    if len(arquivos) > 0:
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(caminho+"\\acoes", arquivo)
            try:
                os.remove(caminho_arquivo)
                print(f"Arquivo {arquivo} removido com sucesso.")
            except Exception as e:
                print(f"Erro ao remover arquivo {arquivo}: {e}")

def retornarAcoes(acoes):
    arquivos = os.listdir(caminho+"\\acoes")
    acoes_baixadas = []

    if len(arquivos) > 0:
        for arquivo in arquivos:
            if "".join(os.path.splitext(arquivo)[0]) in acoes:
                acoes_baixadas.append("".join(os.path.splitext(arquivo)[0]))

    return acoes_baixadas

def BaixarHistorico():
    apagarHistorico()
    acoes = ["RRRP3.SA", "ALPA4.SA", "ABEV3.SA", "ARZZ3.SA", "ASAI3.SA", "AZUL4.SA", "B3SA3.SA", "BBSE3.SA",
         "BBDC3.SA", "BBDC4.SA", "BRAP4.SA", "BBAS3.SA", "BRKM5.SA", "BRFS3.SA", "BPAC11.SA", "CRFB3.SA", "BHIA3.SA",
         "CCRO3.SA", "CMIG4.SA", "CIEL3.SA", "COGN3.SA", "CPLE6.SA", "CSAN3.SA", "CPFE3.SA", "CMIN3.SA", "CVCB3.SA",
         "CYRE3.SA", "DXCO3.SA", "ELET3.SA", "ELET6.SA", "EMBR3.SA", "ENGI11.SA", "ENEV3.SA", "EGIE3.SA", "EQTL3.SA",
         "EZTC3.SA", "FLRY3.SA", "GGBR4.SA", "GOAU4.SA", "GOLL4.SA", "NTCO3.SA", "SOMA3.SA", "HAPV3.SA", "HYPE3.SA",
         "IGTI11.SA", "IRBR3.SA", "ITSA4.SA", "ITUB4.SA", "JBSS3.SA", "KLBN11.SA", "RENT3.SA", "LWSA3.SA", "LREN3.SA",
         "MGLU3.SA", "MRFG3.SA", "BEEF3.SA", "MRVE3.SA", "MULT3.SA", "PCAR3.SA", "PETR3.SA", "PETR4.SA", "RECV3.SA",
         "PRIO3.SA", "PETZ3.SA", "RADL3.SA", "RAIZ4.SA", "RDOR3.SA", "RAIL3.SA", "SBSP3.SA", "SANB11.SA", "SMTO3.SA",
         "CSNA3.SA", "SLCE3.SA", "SUZB3.SA", "TAEE11.SA", "VIVT3.SA", "TIMS3.SA", "TOTS3.SA", "UGPA3.SA", "USIM5.SA",
         "VALE3.SA", "VAMO3.SA", "VBBR3.SA", "WEGE3.SA", "YDUQ3.SA"]


    servico = Service(ChromeDriverManager().install())

    chrome_options = webdriver.ChromeOptions()

    # Configurar o local de download
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": caminho + "\\acoes",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    chrome_options.add_argument('--headless') 

    navegador = webdriver.Chrome(service=servico, options=chrome_options)

    for acao in acoes:
        navegador.get("https://finance.yahoo.com/quote/{}/history".format(acao))
        navegador.find_element('xpath', '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/div[1]/div/div/div').click()
        navegador.find_element('xpath', '//*[@id="dropdown-menu"]/div/ul[2]/li[4]/button').click()
        navegador.find_element('xpath', '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a').click()

        # Aguardar alguns segundos para permitir o download
        time.sleep(1)

    # Fechar o navegador quando terminar
    navegador.quit()

    retorno = retornarAcoes(acoes)

    return retorno


