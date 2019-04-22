# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("/Users/gabrielcaschera/Documents/2013-11-03_tromso_stromsgodset_agg_first.csv")

# Mostrando as primeiras 5 linhas
dataset.head()

# Renomeando as colunas para os nomes corretos das variáveis
dataset.columns = ['timestamp','tag_id','total_distance','hir_distance','sprint_distance','total_effort']

sns.set(style = "whitegrid")

f, ax = plt.subplots(figsize = (6,15))

dataset.sort_values("total_distance", ascending=False)

# Apresentando gráfico com distância total
sns.set_color_codes("pastel")
sns.barplot(x="tag_id", y="total_distance",data=dataset,label="Total distance", color="b")

# Apresentando a distância corrida, sobreposta 
sns.set_color_codes("muted")
sns.barplot(x="tag_id", y="sprint_distance", data=dataset,label="Sprint distance", color="b")

#Adicionando legenda e informações 
ax.legend(ncol=2, loc="top right", frameon=True)
ax.set(xlim=(-2,15), ylabel="Distance in meters", xlabel="Players' tag id")
sns.despine()