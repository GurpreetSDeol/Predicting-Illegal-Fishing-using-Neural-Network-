DROP TABLE IF EXISTS temp_ships_in_ocean, filtered_ship_data ;

CREATE TEMP TABLE temp_ships_in_ocean AS
SELECT DISTINCT mmsi, DATE(timestamp) AS day
FROM ship_data
WHERE is_fishing >= 0
AND EXISTS (
    SELECT 1
    FROM ocean_boundaries
    WHERE ST_Intersects(ship_data.geometry, ocean_boundaries.geometry)
);

SELECT COUNT(*) FROM temp_ships_in_ocean;

CREATE TABLE filtered_ship_data AS
SELECT *
FROM ship_data
WHERE (mmsi, DATE(timestamp)) IN (SELECT mmsi, day FROM temp_ships_in_ocean);


SELECT COUNT(*) FROM filtered_ship_data;

DELETE FROM filtered_ship_data
WHERE is_fishing = -1;