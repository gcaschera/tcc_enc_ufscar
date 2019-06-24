#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 18:19:29 2019

@author: gabrielcaschera
"""
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os 

def verify_results_folder():
    '''
    
        Funcao para verificacao da existencia da pasta; se nao existir, cria 
    
    '''
    
    if not os.path.exists(os.getcwd()+'/results'):
        try: 
            os.makedirs(os.getcwd()+'/results')
            return True
        except:
            return False
    else:     
        return True 

def describe_df(df):
    '''
    
    Funcao que retorna a descricao e as informacoes do dataset 
    
    ''' 
    
    return df.describe(), df.head(), df.info()

def print_plot_png(sns_plot, title, x_name, y_name, hue_name=None):
    '''
    
    Funcao que altera os nomes dos eixos e imprime o grafico para png 
    
    ''' 
    # Define nome do plot com base nas variaveis 
    plt_file_name = 'plt'
    if x_name:
        plt_file_name = plt_file_name + '_' + x_name
    if y_name:
        plt_file_name = plt_file_name + '_' + y_name
    # Se possuir legenda para sub grupos, a mesma e colocada 
    if hue_name:
        sns_plot.legend(title=hue_name)
        plt_file_name = plt_file_name + '_' + hue_name
    
    # Alteracao do titulo do grafico
    if title:
        sns_plot.set_title(label=title)
        
     # Alteracao dos titulos do eixos
    if y_name:
        sns_plot.set_ylabel(y_name, fontsize=12, fontname='Times New Roman')
    if x_name: 
        sns_plot.set_xlabel(x_name, fontsize=12, fontname='Times New Roman')
    
    # Tenta salvar a figura: se conseguir, True; senao, False 
    sns_plot_fig = sns_plot.get_figure()
    try: 
        sns_plot_fig.savefig(os.getcwd()+'/results/'+plt_file_name+'.png')
        print('Sucesso')
        return True
    except: 
        print('Erro para geracao da imagem.')
        return False 

def generate_bar(df, target_column_y, y_name, title, target_column_x = None, x_name = None, palette='GnBu_d'):
    '''
    
    Funcao que imprime o grafico de barras num arquivo .png e retorna True em caso de sucesso
    
    '''
    # Geracao do grafico atraves da biblioteca Seaborn
    # Se nao for dado um valor para o eixo x, e gerado o grafico somente para o y; caso contrario, imprime o x
    if not(target_column_x):
        sns_plot = sns.barplot(y = df[target_column_y], palette=sns.color_palette(palette))
    else:
        sns_plot = sns.barplot(x = df[target_column_x], y = df[target_column_y], palette=sns.color_palette("GnBu_d"))
    # Tenta renomear os eixos e salvar o grafico num arquivo png 
    return print_plot_png(sns_plot, title, x_name, y_name)

def generate_hist(df, target_column, x_name, y_name, title, palette='blue'):
    '''
    
    Funcao que imprime o histograma num arquivo .png e retorna True em caso de sucesso
    
    '''
    # Geracao do grafico atraves da biblioteca Seaborn
    sns_plot = sns.distplot(df[target_column], kde=False, rug=False, color = palette)
    # Tenta renomear os eixos e salvar o grafico num arquivo png 
    return print_plot_png(sns_plot, title, x_name, y_name)
    
def generate_line(df, target_column_x, target_column_y, x_name, y_name, title, hue_column = None, hue_name = None, palette='GnBu_d'):  
    '''
    
    Funcao que imprime o grafico de linhas num arquivo .png e retorna True em caso de sucesso
    
    '''
    # Geracao do grafico atraves da biblioteca Seaborn
    if hue_column:
        sns_plot = sns.lineplot(x=target_column_x, y=target_column_y, hue=hue_column, style=hue_column, data=df, palette=sns.color_palette(palette, n_colors=df[hue_column].nunique()))
    else:
        sns_plot = sns.lineplot(x=target_column_x, y=target_column_y, data=df, palette=sns.color_palette(palette, n_colors=2))
    # Tenta renomear os eixos e salvar o grafico num arquivo png 
    return print_plot_png(sns_plot, title, x_name, y_name, hue_name)

def generate_scatter(df, target_column_x, target_column_y, x_name, y_name, title, palette='GnBu_d'):  
    '''
    
    Funcao que imprime o grafico de dispersao num arquivo .png e retorna True em caso de sucesso
    
    '''
    # Geracao do grafico atraves da biblioteca Seaborn
    sns_plot = sns.scatterplot(x=target_column_x, y=target_column_y, data=df, palette=sns.color_palette(palette))
    
    # Tenta renomear os eixos e salvar o grafico num arquivo png 
    return print_plot_png(sns_plot, title, x_name, y_name)
    
def generate_boxplot(df, target_column_y, y_name, title, target_column_x = None, x_name = None, palette='GnBu_d'):  
    '''
    
    Funcao que imprime o box plot num arquivo .png e retorna True em caso de sucesso
    
    '''
    # Geracao do grafico atraves da biblioteca Seaborn
    if not(target_column_x):
        sns_plot = sns.boxplot(y=df[target_column_y], width=0.5, palette=sns.color_palette(palette))
    else:
        sns_plot = sns.boxplot(y=df[target_column_y], x=df[target_column_x], width=0.5, palette=sns.color_palette(palette))
        
    # Tenta renomear os eixos e salvar o grafico num arquivo png 
    return print_plot_png(sns_plot, title, x_name, y_name)
    
def generate_violin(df, target_column_y, y_name, title, target_column_x = None, x_name = None, palette='GnBu_d'):  
    '''
    
    Funcao que imprime o grafico de linhas num arquivo .png e retorna True em caso de sucesso
    
    '''
    # Geracao do grafico atraves da biblioteca Seaborn
    if not(target_column_x):
        sns_plot = sns.violinplot(y=df[target_column_y], data = df, palette=sns.color_palette(palette, n_colors=2))
    else:
        sns_plot = sns.violinplot(y=df[target_column_y], x=df[target_column_x], data = df, palette=sns.color_palette(palette))
        
    # Tenta renomear os eixos e salvar o grafico num arquivo png 
    return print_plot_png(sns_plot, title, x_name, y_name)