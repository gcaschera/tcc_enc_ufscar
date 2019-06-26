#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 18:29:44 2019

@author: gabrielcaschera

Este arquivo tem como objetivo a geracao dos graficos apresentados no texto do trabalho 
"""

import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Importação do dataset 
df_nba = pd.read_csv('/Users/gabrielcaschera/Downloads/all_seasons.csv')
df_nba_16 = df_nba[df_nba.season=='2016-17'][df_nba.age>30]

# Plot do gráfico de dispersão 
plt2 = sns.scatterplot(x="player_height", y="player_weight", data=df_nba_16)

# Plot do box plot das varíaveis 
for column in df_nba.columns:
    print(column)
    if(column in ('age', 'player_height', 'player_weight', 'gp', 'pts', 'reb', 'ast', 'net_rating')):
        plt2 = sns.boxplot(y=df_nba[column])
        plt.show()
    
# Box plot de idade por temporada da NBA 
sns_plot = sns.boxplot(y=df_nba['age'], x=df_nba['season'], width=0.5)
sns.despine()
sns_plot.set_xticklabels(rotation=30, labels=df_nba['season'].unique())
sns_plot_fig = sns_plot.get_figure()
sns_plot_fig.set_size_inches(11.7, 8.27)
sns_plot_fig.savefig('/Users/gabrielcaschera/Documents/TCC/visualizacoes/box_plot_age.png')
plt.show()

# Matriz de correlação 
corr = df_nba_16.corr()
sns.heatmap(corr, 
        xticklabels=corr.columns,
        yticklabels=corr.columns)

# Análise do Starbucks 
df_star_menu = pd.read_csv('/Users/gabrielcaschera/Downloads/starbucks_drinkMenu_expanded.csv')
df_star_menu_avg = df_star_menu.loc[:,['Beverage_category', 'Calories']].groupby(['Beverage_category']).mean().reset_index()
plt_hist_star_menu = sns.barplot(x = df_star_menu_avg['Beverage_category'], y = df_star_menu_avg['Calories'], palette=sns.color_palette("GnBu_d"))
plt_hist_star_menu.set_xticklabels(rotation=30, labels=df_star_menu_avg['Beverage_category'].unique())
sns_plot_fig = plt_hist_star_menu.get_figure()
sns_plot_fig.set_size_inches(14.7, 14.27)
sns_plot_fig.savefig('/Users/gabrielcaschera/Documents/TCC/visualizacoes/calories_beverage.png')
plt.show()

# Análise do McDonlad's 
# https://www.kaggle.com/mcdonalds/nutrition-facts/
df_mc_menu = pd.read_csv('/Users/gabrielcaschera/Downloads/menu_mc.csv')
target_column = 'Calories'
plt_hist_mc_menu = sns.distplot(df_mc_menu[target_column], kde=False, rug=False, color = 'darkcyan')
sns_plot_fig = plt_hist_mc_menu.get_figure()
sns_plot_fig.set_size_inches(14.7, 14.27)
sns_plot_fig.savefig('/Users/gabrielcaschera/Documents/TCC/visualizacoes/'+target_column+'.png')
plt.show()
print('Mean: '+str(df_mc_menu[target_column].mean())+' -- Median: '+str(df_mc_menu[target_column].median()))

# Análise do Mercado de Ações de Nova York
# https://www.kaggle.com/dgawlik/nyse/downloads/nyse.zip/3
df_nyse = pd.read_csv('/Users/gabrielcaschera/Downloads/nyse/prices.csv', usecols=['date','close','symbol'], parse_dates=['date'])
df_nyse_amzn_temp = df_nyse[df_nyse.symbol=='AMZN'][df_nyse.date > '2015-12-31']
df_nyse_amzn = df_nyse_amzn_temp[['date','close']]
y_column = 'close'
x_column = 'date'
plt_hist_nyse = sns.lineplot(x=x_column, y=y_column, data=df_nyse_amzn[[x_column, y_column]])
plt_hist_nyse.set_xticklabels(rotation=90, labels=df_nyse_amzn['date'])
plt_hist_nyse.xaxis.set_major_locator(mdates.WeekdayLocator())
plt_hist_nyse.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
plt_hist_nyse.set_ylabel("Preço no fechamento",fontsize=12, fontname='Times New Roman')
plt_hist_nyse.set_xlabel("Data",fontsize=12, fontname='Times New Roman')
sns_plot_fig = plt_hist_nyse.get_figure()
sns_plot_fig.set_size_inches(14.7, 14.27)
sns_plot_fig.savefig('/Users/gabrielcaschera/Documents/TCC/visualizacoes/df_nyse_amzn.png')
plt.show()

# Gráfico 2: comparação de valor de ações 
df_nyse_comp = df_nyse[(df_nyse.symbol=='AMZN') | (df_nyse.symbol=='GOOGL') | (df_nyse.symbol=='AAPL')][df_nyse.date > '2015-12-31']
y_column = 'close'
x_column = 'date'
hue_column = 'symbol'
plt_hist_nyse = sns.lineplot(x=x_column, y=y_column, hue=hue_column, style=hue_column, data=df_nyse_comp, palette=sns.color_palette("GnBu_d", n_colors=3))
plt_hist_nyse.set_xticklabels(rotation=90, labels=df_nyse_amzn['date'])
plt_hist_nyse.xaxis.set_major_locator(mdates.WeekdayLocator())
plt_hist_nyse.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
plt_hist_nyse.legend(title='Empresa', labels=['Apple (AAPL)', 'Amazon (AMZN)', 'Google (GGOGL)'])
plt_hist_nyse.set_ylabel("Preço no fechamento",fontsize=12, fontname='Times New Roman')
plt_hist_nyse.set_xlabel("Data",fontsize=12, fontname='Times New Roman')
sns_plot_fig = plt_hist_nyse.get_figure()
sns_plot_fig.set_size_inches(14.7, 14.27)
sns_plot_fig.savefig('/Users/gabrielcaschera/Documents/TCC/visualizacoes/df_nyse_comp.png')
plt.show()

# us-education-datasets-unification-project
# https://www.kaggle.com/noriuk/us-education-datasets-unification-project/
df_us_educ_org = pd.read_csv('/Users/gabrielcaschera/Downloads/us-education-datasets-unification-project/states_all.csv')
df_us_educ = df_us_educ_org[df_us_educ_org.YEAR == 2015]
y_column = 'TOTAL_REVENUE'
x_column = 'GRADES_ALL_G'
plt_us_educ = sns.scatterplot(x=x_column, y=y_column, data=df_us_educ, palette=sns.color_palette("GnBu_d", n_colors=3))
plt_us_educ.set_ylabel("Receita total (milhòes de US$)",fontsize=12, fontname='Times New Roman')
plt_us_educ.set_xlabel("Número total de alunos",fontsize=12, fontname='Times New Roman')
sns_plot_fig = plt_us_educ.get_figure()
sns_plot_fig.set_size_inches(14.7, 14.27)
sns_plot_fig.savefig('/Users/gabrielcaschera/Documents/TCC/visualizacoes/plt_us_educ.png')
plt.show()
# Matriz de correlação 
corr = df_us_educ.corr(method='pearson')
sns.heatmap(corr, 
        xticklabels=corr.columns,
        yticklabels=corr.columns)

# Violin plots utilizando dados de idade da NBA
sns_plot = sns.violinplot(y=df_nba['age'], x=df_nba['season'], width=0.5)
sns.despine()
sns_plot.set_xticklabels(rotation=30, labels=df_nba['season'].unique())
sns_plot_fig = sns_plot.get_figure()
sns_plot_fig.set_size_inches(14.7, 10.39)
sns_plot_fig.savefig('/Users/gabrielcaschera/Documents/TCC/visualizacoes/nba_violin_plot_age.png')
plt.show()

# Brooklyn houses price sales analysis 
# https://www.kaggle.com/tianhwu/brooklynhomes2003to2017/
df_housesBklyn = pd.read_csv('/Users/gabrielcaschera/Downloads/brooklynhomes2003to2017/brooklyn_sales_map.csv')
df_housesBklyn2017 = df_housesBklyn[df_housesBklyn.year_of_sale == 2012]
sns_plot = sns.violinplot(y=df_housesBklyn2017['sale_price'])
sns.despine()
sns_plot_fig = sns_plot.get_figure()
sns_plot_fig.savefig('/Users/gabrielcaschera/Documents/TCC/visualizacoes/housesBklyn_salesPrice.png')
plt.show()

# Análise de milimitros de chuva na Australia
# https://www.kaggle.com/jsphyg/weather-dataset-rattle-package/
df_rainAUS = pd.read_csv('/Users/gabrielcaschera/Downloads/weatherAUS.csv')
target_column = 'Rainfall'
sns_plot = sns.violinplot(y=df_rainAUS[target_column], data = df_rainAUS, palette=sns.color_palette("GnBu_d", n_colors=2))
sns.despine()
sns_plot_fig = sns_plot.get_figure()
sns_plot_fig.savefig('/Users/gabrielcaschera/Documents/TCC/visualizacoes/rainAUS_'+target_column+'.png')
plt.show()