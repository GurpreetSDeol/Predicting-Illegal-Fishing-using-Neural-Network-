# Predicting-Illegal-Fishing-using-Neural-Network-


The aim of this project is to predict illegal fishing using machine learning. Fishing can be classified as illegal for various reasons, including the type of fishing gear, fishing season, overfishing, fishing in Marine Protected Zones (MPZ), misreporting catch, and fishing endangered species, to name a few. However, due to the limits of available data, I will only be focusing on MPZs in the ocean (due to computational limits).

The data used for this project is freely available on Global Fishing Watch (ship vessel data), Natural Earth Data (ocean boundaries), and Protected Planet (MPZ boundaries). The vessel data has been preprocessed with an is_fishing label to identify if a vessel is fishing at that instant or not.

As it is mandatory for shipping vessels to have a tracker, we can use their journey logs and cross-reference them with the geometric data of MPZs to see if they traveled through the MPZ and fished in these waters. Using this, we can manually create a label for illegal fishing (yes or no) if the ship had traveled through and fished in an MPZ after it had been established. Using this data, I built a neural network algorithm to predict illegal fishing activity with an accuracy of 97%.
