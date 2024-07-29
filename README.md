# Predicting-Illegal-Fishing-using-Neural-Network-


# Overview
The aim of this project is to predict illegal fishing using machine learning. Fishing can be classified as illegal for various reasons, including the type of fishing gear, fishing season, overfishing, fishing in Marine Protected Zones (MPZ), misreporting catch, and fishing endangered species, to name a few. However, due to the limits of available data, this project focuses on MPZs in the ocean.

# Data Sources
Global Fishing Watch: Ship vessel data, including preprocessed labels indicating if a vessel is fishing.
Natural Earth Data: Ocean boundaries data.
Protected Planet: Marine Protected Zones (MPZ) boundaries.
Project Structure

# Folders
Algorithm
Contains the Jupyter notebook for building and training the neural network model.
Data Processing
SQL and Jupyter notebooks for creating the database, loading data, and classifying fishing activity.
Plots
Visual representation of MPZs.

# Repository Contents

Algorithm/

Neural Network.ipynb: Jupyter notebook to train and evaluate the neural network model.

Data Processing/

Create_Database.sql: SQL script to create the PostgreSQL database and necessary tables.

Filter_ship_data.sql: SQL script to filter and preprocess ship data.

Illegal_Fishing_Classification.sql: SQL script to classify fishing activity as legal or illegal.

Load_gdb_data.ipynb: Jupyter notebook to load geospatial data into the database.

load_shp_to_psql.sql: SQL script to load shapefile data into PostgreSQL.

Plots/

MPZ+Plot.png: Image showing the plot of Marine Protected Zones.
