#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 14:18:36 2019

@author: gabrielcaschera
"""

def read_csv_file():
    """
    
    Função para leitura do arquivo csv a partir do sistema de arquivos do computador.
    Retorna o arquivo lido pelo pandas.read_csv
    
    """
    
    import tkinter as tk
    from tkinter import filedialog
    import pandas as pd

    # Leitura do arquivo csv
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename() 
    
    if '.csv' not in file_path:
        print('Favor informar um arquivo .csv. O arquivo ', file_path, ' nao esta nesse formato.')
        file_path = filedialog.askopenfilename() 
        
    #input('Pressione Enter para Continuar')
    
    return pd.read_csv(file_path, sep=';')
    


def describe_df(df):
    """
    
    Função que retorna a descrição e as informações do dataset. 
    
    """ 
    
    return df.describe()

def generate_hist(df, var, x_name, y_name, title):
    import plotly.plotly as py 
    import plotly.graph_objs as go
    from plotly.offline import plot, iplot, init_notebook_mode
    # Using plotly + cufflinks in offline mode
    import cufflinks
    cufflinks.go_offline(connected=True)
    init_notebook_mode(connected=True)
    
    #df[var].plot(kind='hist', xTitle=x_name, yTitle=y_name, title=title)
    plotly.offline.plot({
    "data": [go.Histogram(y=df[var])],
    "layout": go.Layout(title=title)
}, auto_open=True)