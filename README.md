# Predicting-Illegal-Fishing-using-Neural-Network-

The aim of this project is to predict illegal fishing using machine learning. Fishing can be classified as illegal depending on various reasons which includes: type pf fishing gear, fishing season, overfishing, fishing in Marine protected zones (MPZ), misreporting catch, fishing endagred species to name a few. However, due to the limits of data avaiable, I will only be focusing on MPZs in the ocean (due to computational limits) 

The data used for this projecetd is freely avaiavlble on Glonbal Fishing watch(Ship vessel data), Natural earth data(Ocean boundaries) and Protected Planet(MPZ boundaries). The vessel data has been preprocessed with a is_fishing label to identify if a vessel is fishing at that instant or not. 

As it is mandotary for shipping vessels to have a tracker, we can use thier journey logs and cross reference them with the geometric data of MPZs to see if they travelled through the MPZ and fished in these waters. Using this we can manually create a label for illegal fishing (yes or no) if the ship had travlled throgh anf dished in a MPZ after it had been estavlished. Using this data I built a neural network algorithm to predict illegal fishing activity with an accuracy of 97%.

