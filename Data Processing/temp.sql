SELECT illegal, COUNT(*) as count
FROM filtered_ship_data
GROUP BY illegal;
