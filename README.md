# Predicting-Illegal-Fishing-using-Random-Forest-

# Update  22/10/2024

# Overview

I reduced the scope of the project to focus only on the North East Atlantic Ocean and changed my approach. I created a Random Forest algorithm to predict if a ship is fishing or not, depending on a few variables. The accuracy of the algorithm was 97%. I implemented an API to obtain more vessel data, process it, and use the algorithm to make a prediction on the fishing status. Then, I filtered the location through the NEA polygon and the NEA MPZ polygon and point data to see if the vessels were in these waters. If they were and were fishing, they would be classified as illegal.


# Data Sources
Global Fishing Watch: Ship vessel data and API, including preprocessed labels indicating if a vessel is fishing.
Natural Earth Data: Ocean boundaries data.
Protected Planet: .shp files containing Marine Protected Zones (MPZ) boundaries.

# Repository Contents

__Analysis.ipynb__: Jupyter notebook containing the analysis of fishing events data.

__Plots__: Contains plots.

__Filter_Fishing_data.ipynb__: Filter through the files of ship data, cleaning and merging them.

__Filter_MPZ_data.ipynb__: Filter through the MPZs in the North East Atlantic Ocean

__Main.ipynb__: Contains the Random Forest Model as well as the API and classification 

# Future Work
Real-time Tracking API: Plan to implement an API to track vessels in real-time, providing timely predictions of illegal fishing activities.

Enhancements: Continuously improve the model's accuracy and incorporate additional data sources for better predictions.

# Update  17/10/2024
The scope of the original project, which includes all of the oceans and lakes, has proven to be a challenging endeavor due to limited resources. This has also impacted my ability to train the ML algorithm with reasonable accuracy. Consequently, I will scale down the project to focus on a specific ocean. Additionally, I plan to implement more methods for classifying fishing as illegal, including considering fishing seasons and any other relevant metrics I can acquire.

#Previous Overview
The aim of this project is to predict illegal fishing using machine learning. Fishing can be classified as illegal for various reasons, including the type of fishing gear, fishing season, overfishing, fishing in Marine Protected Zones (MPZ), misreporting catch, and fishing endangered species, to name a few. However, due to the limits of available data, this project focuses on illegal fishing in MPZs in the ocean and major lakes. 

For the algorithm, the data was assigned 1 of 3 labels for illegal fishing; 

- 'yes' if during the timestamp of the event, the ship was fishing, its coordinates were in an established MPZ, and the timestamp year is equal or greater than the year the MPZ was established.
- 'maybe' if during the timestamp of the event, the ship was not fishing but its coordinates were in an established MPZ and the timestamp year is equal or greater than the year the MPZ was established.
- 'no' if the ship was not in an established MPZ during the fishing event.ot in an established MPZ during the fishing event. 
