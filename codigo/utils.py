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

def generate_plt():
    