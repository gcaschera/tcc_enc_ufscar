# Creation of tool to help with visualization and exploratory analysis of datasets

Repository of the graduation paper of the Computer Engineering course (Federal University of São Carlos).

Autor: Gabriel Teixeira Caschera 

## Project description

This project has the goal to create a tool that helps in the visualization and exploratory analysis of data present in a given dataset. The motivation for building this tool comes from the increasing availability and generation of data and the interest to create automatic tools to extract information from it. Therefore, this tool can help in this task, in a way that the analyst does not has to program directaly in a programming language, like Python or R. 

The tool is created using the Python programming language and the Pandas, Seaborn and Matplotlib libraries. 

## Repository organization

This repository is divided in two main folders: "codigo" and "visualizacoes". 

### Codigo 

This folder contains the source codes created in order to build the tool (*data_visualization_tool.py*) and generate some examples of the visualizations considered (*data_visualization_generator.py*). The charts considered are histograms, bar, line, scatter, box and violin plots. The *main.py* code is the code that implements the graphic interface in which the user can interact and generate the plots. This interface is implemented with the help of the Tkinter library. 

### Visualizacoes 

This folder has the visualizations generated as examples (via the *data_visualization_generator.py*). 
