# Predicting-Illegal-Fishing-using-Neural-Network-


# Overview
The aim of this project is to predict illegal fishing using machine learning. Fishing can be classified as illegal for various reasons, including the type of fishing gear, fishing season, overfishing, fishing in Marine Protected Zones (MPZ), misreporting catch, and fishing endangered species, to name a few. However, due to the limits of available data, this project focuses on MPZs in the ocean.

# Data Sources
Global Fishing Watch: Ship vessel data, including preprocessed labels indicating if a vessel is fishing.
Natural Earth Data: Ocean boundaries data.
Protected Planet: Marine Protected Zones (MPZ) boundaries.
Project Structure

# Folders
API and AWS:

Contains the test files for the global fishing watch API.

Algorithm:
Contains the Jupyter notebook for building and training the neural network model.

Data Analysis:
Contains plots and analysis of the data.

Data Processing:
SQL and Jupyter notebooks for creating the database, loading data, and classifying fishing activity.

# Repository Contents

Algorithm/

Neural Network.ipynb: Jupyter notebook to train and evaluate the neural network model.

API and AWS/ 
Test Api.py: Python file for making a request to the API

Data Analysis/ 

Analysis.ipynb: Jupyter notebook containing the analysis of fishing events data.
Plots: Contains plots.

Data Processing/

Create_Database.sql: SQL script to create the PostgreSQL database and necessary tables.

Filter_ship_data.sql: SQL script to filter and preprocess ship data.

Illegal_Fishing_Classification.sql: SQL script to classify fishing activity as legal or illegal.

Load_gdb_data.ipynb: Jupyter notebook to load geospatial data into the database.

load_shp_to_psql.sql: SQL script to load shapefile data into PostgreSQL.



# Future Work
Real-time Tracking API: Plan to implement an API to track vessels in real-time, providing timely predictions of illegal fishing activities.

Enhancements: Continuously improve the model's accuracy and incorporate additional data sources for better predictions.
