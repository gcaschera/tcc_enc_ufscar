#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 14:23:05 2019

@author: gabrielcaschera
"""

import utils
import data_visualization_tool as datavis
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as scrolledtext
from tkinter import messagebox
    
def create_input_boxes():
    '''
    
        Funcao que cria as caixas de entrada de texto para input dos parametros pelo usuario 
        
    '''
    fields = ['target_column_x', 'x_name','target_column_y', 'y_name', 'title', 'hue_column', 'hue_name']
    entries = []
    for field in fields:
        row = tk.Frame(window)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries
            
def fetch(entries):
    '''
    
        Funcao que busca os valores dos parametros fornecidos pelo usuario 
    
    '''
    # Resgata os valores inseridos 
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        fields_values[field] = text
    
    # Registra os valores no log
    for field, value in fields_values.items():
        print('%s: "%s"' % (field, value)) 
    
    # Verifica qual o grafico solicitado pelo usario e chama a respectiva funcao da ferramenta
    if fields_values['plot_type'] == 'histograma':
        if datavis.generate_hist(df = df, target_column = fields_values['target_column_y'], x_name = fields_values['x_name'], 
                                 y_name = fields_values['y_name'], title = fields_values['title']):
            messagebox.showinfo('Sucesso', 'Grafico gerado com sucesso!')
        else:
            messagebox.showerror('Erro de execucao', 'Erro ao gerar o grafico.')
            
    elif fields_values['plot_type'] == 'linha':
        if datavis.generate_line(df=df, target_column_x = fields_values['target_column_x'], target_column_y = fields_values['target_column_y'], 
                                 x_name = fields_values['x_name'], y_name = fields_values['y_name'], title = fields_values['title'],
                                 hue_column = fields_values['hue_column'], hue_name = fields_values['hue_name']):
            messagebox.showinfo('Sucesso', 'Grafico gerado com sucesso!')
        else:
            messagebox.showerror('Erro de execucao', 'Erro ao gerar o grafico.')
            
    elif fields_values['plot_type'] == 'dispersao':
        if datavis.generate_scatter(df = df, target_column_x = fields_values['target_column_x'], target_column_y = fields_values['target_column_y'], 
                                    x_name = fields_values['x_name'], y_name = fields_values['y_name'], title = fields_values['title']):
            messagebox.showinfo('Sucesso', 'Grafico gerado com sucesso!')
        else:
            messagebox.showerror('Erro de execucao', 'Erro ao gerar o grafico.')
            
    elif fields_values['plot_type'] == 'boxplot':
        if datavis.generate_boxplot(df = df, target_column_x = fields_values['target_column_x'], target_column_y = fields_values['target_column_y'], 
                                    x_name = fields_values['x_name'], y_name = fields_values['y_name'], title = fields_values['title']):
            messagebox.showinfo('Sucesso', 'Grafico gerado com sucesso!')
        else:
            messagebox.showerror('Erro de execucao', 'Erro ao gerar o grafico.')
            
    elif fields_values['plot_type'] == 'violin':
        if datavis.generate_violin(df = df, target_column_x = fields_values['target_column_x'], target_column_y = fields_values['target_column_y'], 
                                    x_name = fields_values['x_name'], y_name = fields_values['y_name'], title = fields_values['title']):
            messagebox.showinfo('Sucesso', 'Grafico gerado com sucesso!')
        else:
            messagebox.showerror('Erro de execucao', 'Erro ao gerar o grafico.')
            
    else: # barra
        if datavis.generate_bar(df = df, target_column_x = fields_values['target_column_x'], target_column_y = fields_values['target_column_y'], 
                                    x_name = fields_values['x_name'], y_name = fields_values['y_name'], title = fields_values['title']):
            messagebox.showinfo('Sucesso', 'Grafico gerado com sucesso!')
        else:
            messagebox.showerror('Erro de execucao', 'Erro ao gerar o grafico.')

def instructions():
    '''
    
        Funcao para mostrar instrucoes de utilizacao da ferramenta 
    
    '''
    # Define mensagem 
    msg = 'Utilizacao:\ntarget_column_x: coluna plotada em x\ntarget_column_y: coluna plotada em y\n'
    msg = msg+'x_name: nome do eixo x\ny_name: nome do eixo y\ntitle: titulo do grafico\nhue: coluna para clusters'
    msg = msg+'\nhue_name: nome da legenda dos clusters'
    # Cria a janela de mensagem 
    messagebox.showinfo('Instrucoes de uso', msg)

def describe_df(df):
    '''
    
        Funcao para apresentar a descricao do dataframe numa nova janela 
        A descricao e chamada da ferramenta 
    
    '''
    # Coleta informacoes atraves da ferramenta 
    desc, head, info = datavis.describe_df(df)
    print('Desc: \n', desc, '\nHead:\n', head, '\nInfo:\n', str(info))
    info = 'Desc: \n'+ str(desc)+ '\nHead:\n'+ str(head)+ '\nInfo:\n'+ str(info)
    
    # Criacao da janela de output de informacoes
    desc_win = tk.Tk()
    desc_win.title('Descricao do DataSet')
    desc_win.geometry('360x300')
    
    # Apresentacao das informacoes na janela de texto
    st_desc = scrolledtext.ScrolledText(desc_win, width=360,height=300)
    st_desc.insert('insert', info)
    st_desc.pack(fill='both')

    desc_win.mainloop()
    
def cb_update_field(index):
    '''
    
        Funcao para atualzar o valor do plot_type atrelado ao combobox 
    
    '''
    fields_values['plot_type'] = combo.get()
    print('Combobox atualizado para: ', combo.get())

if __name__ == '__main__':
    
    # Mensagem de inicio no log
    print('Ferramenta para Analise de Datasets')
    
    # Cria pasta de resultados, caso a mesma nao exista
    if not datavis.verify_results_folder():
        print('Erro na criacao da pasta. Encerrar.')
    
    # Solicita leitura do dataframe
    df, success = utils.read_csv_file() 
    if not success: 
        print(utils.close_program('user'))
        messagebox.showwarning('Erro de importação', utils.close_program('user'))
    else:

        # Estruturas de dados com informacoes basicas
        plots = ['barra', 'histograma', 'linha', 'dispersao', 'boxplot', 'violin']
        
        fields_values = dict([
                ('plot_type', ''), 
                ('target_column_x', ''),
                ('x_name', ''),
                ('target_column_y', ''), 
                ('y_name', ''), 
                ('title', ''), 
                ('hue_column', ''), 
                ('hue_name', '')
                ])
        
        # Transformacao das colunas em texto separado por | para apresentacao 
        column_opts = df.columns[0]
        for col in df.columns:
            if col != df.columns[0]: 
                column_opts = column_opts + ' | ' + col 
        
        # Inicializacao e definicoes esteticas da janela 
        window = tk.Tk()
        window.title('Ferramenta para Analise de Datasets')
        window.geometry('600x500')
        
        # Criacao da janela de apresentacao das colunas do dataset 
        st = scrolledtext.ScrolledText(window, width=90,height=6)
        st.insert('insert', 'Colunas importadas:\n'+column_opts.strip())
        st.pack(fill='x')
        
        # Variavel para resgatar valor do ComboBox
        cb_value = tk.StringVar()
        cb_value.trace('w',cb_update_field)
        
        # Criacao do combobox para selecao do grafico 
        combo = ttk.Combobox(window, textvar=cb_value, values=[plots[0], plots[1], plots[2], plots[3], plots[4], plots[5]])
        combo.bind("<<ComboboxSelected>>", cb_update_field)
        combo.current(0)
        combo.pack(fill=tk.X)
        
        # Criacao das caixas de entrada de textos
        entries = create_input_boxes()
        
        # Botoes para acao 
        btns_frm = tk.Frame(window)
        btns_frm.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)
        
        # Instrucoes
        btn_help = tk.Button(btns_frm, text = 'Instrucoes', command=instructions)
        btn_help.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Descricao do dataframe 
        btn_help = tk.Button(btns_frm, text = 'Dados do DataFrame', command=(lambda df=df: describe_df(df)))
        btn_help.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Geracao do grafico 
        btn_plot = tk.Button(btns_frm, text = 'Gerar grafico', command=(lambda e=entries: fetch(e)))
        btn_plot.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Finalizar ferramenta 
        btn_quit = tk.Button(btns_frm, text='Sair', command=window.quit)
        btn_quit.pack(side=tk.LEFT, padx=5, pady=5)
        
        window.mainloop()

    print('Utilizacao encerrada')