#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 14:23:05 2019

@author: gabrielcaschera
"""

import utils

if __name__ == '__main__':
    print('Iniciado execucao do programa')
    
    df = utils.read_csv_file() 
    
    print(df.head())
    
    print('------------')
    
    desc = utils.describe_df(df)
    print('Desc: \n', desc)
    
    var = input('Informe a variavel para ser plotada: ')
    x_name = input('Titulo do X: ')
    y_name = input('Titulo do Y: ')
    title = input('Titulo do Grafico: ')
    utils.generate_hist(df, var, x_name, y_name, title)
    
    input('Esperando por tecla...')
    print('Finalizando execucao do programa')