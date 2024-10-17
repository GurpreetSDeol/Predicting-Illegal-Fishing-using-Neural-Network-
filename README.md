# Predicting-Illegal-Fishing-using-Neural-Network-

# Update  17/10/2024
The scope of the original project, which includes all of the oceans and lakes, has proven to be a challenging endeavor due to limited resources. This has also impacted my ability to train the ML algorithm with reasonable accuracy. Consequently, I will scale down the project to focus on a specific ocean. Additionally, I plan to implement more methods for classifying fishing as illegal, including considering fishing seasons and any other relevant metrics I can acquire.

# Overview
The aim of this project is to predict illegal fishing using machine learning. Fishing can be classified as illegal for various reasons, including the type of fishing gear, fishing season, overfishing, fishing in Marine Protected Zones (MPZ), misreporting catch, and fishing endangered species, to name a few. However, due to the limits of available data, this project focuses on illegal fishing in MPZs in the ocean and major lakes. 

For the algorithm, the data was assigned 1 of 3 labels for illegal fishing; 

- 'yes' if during the timestamp of the event, the ship was fishing, its coordinates were in an established MPZ, and the timestamp year is equal or greater than the year the MPZ was established.
- 'maybe' if during the timestamp of the event, the ship was not fishing but its coordinates were in an established MPZ and the timestamp year is equal or greater than the year the MPZ was established.
- 'no' if the ship was not in an established MPZ during the fishing event.ot in an established MPZ during the fishing event. 

# Data Sources
Global Fishing Watch: Ship vessel data, including preprocessed labels indicating if a vessel is fishing.
Natural Earth Data: Ocean boundaries data.
Protected Planet: .shp files containing Marine Protected Zones (MPZ) boundaries.

# Repository Contents

Analysis.ipynb: Jupyter notebook containing the analysis of fishing events data.

Create_Database.sql: SQL script to create the PostgreSQL database and necessary tables.

Filter_data.ipynb: Filter the .shp files and csv files

Illegal_Fishing_Classification.sql: SQL script to classify fishing activity as legal or illegal.

Neural_Network.py: Python Script to train and evaluate the neural network model.

Neural_Network.keras: Neural Network model 

Plots: Contains plots.

Test Api.ipynb: Current work in progress Jupyter Python file for making a request to the API.



# Future Work
Real-time Tracking API: Plan to implement an API to track vessels in real-time, providing timely predictions of illegal fishing activities.

Enhancements: Continuously improve the model's accuracy and incorporate additional data sources for better predictions.
