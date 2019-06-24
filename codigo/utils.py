#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 14:18:36 2019

@author: gabrielcaschera
"""

import tkinter as tk
from tkinter import filedialog
import pandas as pd

def read_csv_file():
    '''
    
    Funcao para leitura do arquivo csv a partir do sistema de arquivos do computador.
    Retorna o arquivo lido pelo pandas.read_csv
    
    '''

    # Leitura do arquivo csv
    root = tk.Tk()
    root.withdraw()
    root.update()
    file_path = filedialog.askopenfilename() 
    
    # Caso a extensao do arquivo nao seja csv, e esperada a leitura ate o usuario cancelar
    while ('.csv' not in file_path) and (file_path):
        print('Favor informar um arquivo .csv. O arquivo ', file_path, ' nao esta nesse formato.')
        file_path = filedialog.askopenfilename() 
        
    if not file_path:
        return None, False
    else:
        return pd.read_csv(file_path), True

def close_program(close_type):
    '''
    
    Funcao para mensagem de encerramento do programa: retorna string
    Tipos: 
        user: Usuario solicitou encerramento
        error: Erro fatal
        
    '''
    
    closing_answers = {
            'user': 'Usuario solicitou encerramento. Encerrando...',
            'error': 'Erro fatal. Encerrando programa.'
            }
    
    return closing_answers.get(close_type, 'Encerrando...')